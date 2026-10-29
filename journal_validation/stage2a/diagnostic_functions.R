# Isolated instrumentation of the preserved candidates. No numerical settings changed.
dml_detail <- function(y, D, X, Z, tau, a) {
  lambda <- lambda_BC_author(X, R = 1000, tau = tau, c = 2, alpha = 0.1)
  lasso <- quantreg::rq(y - a * D ~ X, tau = tau, method = "lasso", lambda = lambda)
  beta <- matrix(lasso$coefficients, ncol = 1)
  e <- y - a * D - cbind(1, X) %*% beta
  distribition <- diag(c(dnorm(e, mean(e), var(e))))
  density <- diag(distribition)
  distribition <- sqrt(distribition)
  psi <- matrix(0, nrow = length(Z[1, ]), ncol = length(Z[, 1]))
  instrument <- vector("list", ncol(Z))
  for (j in seq_len(length(Z[1, ]))) {
    delta_fit <- hdm::rlasso(distribition %*% Z[, j] ~ distribition %*% X, post = FALSE)
    delta <- matrix(delta_fit$coefficients, ncol = 1)
    delta <- Z[, j] - cbind(1, X) %*% delta
    psi[j, ] <- t(delta)
    instrument[[j]] <- delta_fit[c("coefficients", "lambda", "lambda0", "loadings", "iter", "options")]
  }
  indicator <- ifelse(e <= 0, 1, 0)
  g <- psi %*% (tau - indicator)
  second_moment <- psi %*% diag(diag((tau - indicator) %*% t(tau - indicator))) %*% t(psi)
  invsigma <- solve(second_moment)
  W <- drop(t(g) %*% invsigma %*% g)
  list(W = W, lambda = lambda, beta = beta, e = drop(e), psi = psi,
       density = density, instrument = instrument, condition_second_moment = kappa(second_moment))
}

gmm_detail <- function(y, D, X, Z, tau, a) {
  beta_fit <- quantreg::rq(y - (a * D) ~ X, tau = tau)
  beta <- matrix(beta_fit$coefficients, nrow = 1)
  e <- y - a * D - cbind(1, X) %*% t(beta)
  distribition <- diag(c(dnorm(e, mean(e), var(e))))
  density <- diag(distribition)
  M <- t(Z) %*% distribition %*% X
  J <- t(X) %*% distribition %*% X
  delta <- M %*% solve(J)
  psi <- t(Z) - delta %*% t(X)
  indicator <- ifelse(e <= 0, 1, 0)
  g <- psi %*% (tau - indicator)
  second_moment <- psi %*% diag(diag((tau - indicator) %*% t(tau - indicator))) %*% t(psi)
  invsigma <- solve(second_moment)
  W <- drop(t(g) %*% invsigma %*% g)
  list(W = W, beta = beta, e = drop(e), psi = psi, density = density,
       delta = delta, condition_J = kappa(J), condition_second_moment = kappa(second_moment))
}

# Generate alternatives by replacing precisely one AST node. All other code identical.
sd_variant <- function(fun) {
  count <- 0L
  replace <- function(node) {
    if (identical(node, quote(dnorm(e, mean(e), var(e))))) {
      count <<- count + 1L
      return(quote(dnorm(e, mean(e), sd(e))))
    }
    if (is.call(node)) for (i in seq_along(node)) node[[i]] <- replace(node[[i]])
    node
  }
  body(fun) <- replace(body(fun))
  stopifnot(count == 1L)
  fun
}

object_hash <- function(x) digest::digest(x, algo = "sha256", serialize = TRUE)
state_text <- function(x) paste(x, collapse = ";")
set_stream <- function(state) assign(".Random.seed", state, envir = .GlobalEnv)

safe_fit <- function(fun, dat, controls, tau, state) {
  set_stream(state)
  warnings <- character()
  start <- proc.time()[3]
  value <- tryCatch(withCallingHandlers(
    fun(dat$y, dat$D, controls, dat$Z, tau, alpha_true(tau)),
    warning = function(w) { warnings <<- c(warnings, conditionMessage(w)); invokeRestart("muffleWarning") }),
    error = function(e) list(error = conditionMessage(e)))
  list(value = value, warnings = warnings, rng_after = get(".Random.seed", .GlobalEnv),
       elapsed = unname(proc.time()[3] - start),
       failed = !is.null(value$error) || is.null(value$W) || !is.finite(value$W))
}

pair_task <- function(task) {
  dat <- readRDS(task$data_path)
  initial_hash <- object_hash(dat)
  controls <- if (task$estimator == "Oracle-GMM") dat$X1 else dat$X
  fun <- if (task$estimator == "DML-IVQR-BC") dml_detail else gmm_detail
  # Reconstruct the pivotal draws explicitly; then reset before EACH fit.
  pivotal_hash <- NA_character_; expected_lambda <- NULL
  if (task$estimator == "DML-IVQR-BC") {
    set_stream(task$stream)
    U <- matrix(runif(nrow(dat$X) * 1000), nrow(dat$X))
    pivotal_hash <- object_hash(U)
    sigs <- apply(dat$X, 2, norm2n_author)
    R <- (t(dat$X) %*% (task$tau - (U < task$tau))) / (sigs * sqrt(task$tau * (1-task$tau)))
    expected_lambda <- 2 * quantile(apply(abs(R), 2, max), .9) * sqrt(task$tau*(1-task$tau)) * c(1,sigs)
    rm(U, R)
  }
  base <- safe_fit(fun, dat, controls, task$tau, task$stream)
  alt <- safe_fit(sd_variant(fun), dat, controls, task$tau, task$stream)
  same_data <- identical(initial_hash, object_hash(dat))
  both <- !base$failed && !alt$failed
  beta_equal <- residual_equal <- penalty_equal <- NA
  pivotal_verified <- TRUE
  if (both) {
    beta_equal <- identical(base$value$beta, alt$value$beta)
    residual_equal <- identical(base$value$e, alt$value$e)
    if (task$estimator == "DML-IVQR-BC") {
      penalty_equal <- identical(base$value$lambda, alt$value$lambda)
      pivotal_verified <- identical(base$value$lambda, expected_lambda) && penalty_equal
    }
    stopifnot(beta_equal, residual_equal, pivotal_verified)
  }
  # Explicitly regenerate and hash the alternative's stream as an additional check.
  if (task$estimator == "DML-IVQR-BC") {
    set_stream(task$stream)
    stopifnot(identical(pivotal_hash, object_hash(matrix(runif(nrow(dat$X)*1000), nrow(dat$X)))))
  }
  stopifnot(same_data)
  maxdiff <- function(a,b) if (both) max(abs(a-b)) else NA_real_
  summary <- data.frame(experiment=task$experiment, task_id=task$id, n=nrow(dat$X),
    sample_id=task$sample_id, tau=task$tau, kappa=dat$kappa, estimator=task$estimator,
    stream_index=task$stream_index, worker_pid=Sys.getpid(), data_sha256=initial_hash,
    pivotal_sha256=pivotal_hash, stream=state_text(task$stream),
    paired_data_identical=same_data, paired_beta_identical=beta_equal,
    paired_residuals_identical=residual_equal, paired_penalty_identical=penalty_equal,
    pivotal_verified=pivotal_verified,
    rng_after_identical=identical(base$rng_after,alt$rng_after),
    W_baseline=if(base$failed) NA_real_ else base$value$W,
    W_alternative=if(alt$failed) NA_real_ else alt$value$W,
    failed_baseline=base$failed, failed_alternative=alt$failed,
    error_baseline=if(is.null(base$value$error)) "" else base$value$error,
    error_alternative=if(is.null(alt$value$error)) "" else alt$value$error,
    warnings_baseline=paste(base$warnings,collapse=" | "),
    warnings_alternative=paste(alt$warnings,collapse=" | "),
    density_max_abs_diff=maxdiff(base$value$density,alt$value$density),
    density_rms_diff=if(both) sqrt(mean((base$value$density-alt$value$density)^2)) else NA_real_,
    psi_max_abs_diff=maxdiff(base$value$psi,alt$value$psi),
    instrument_coef_max_abs_diff=if(both) {
      if(task$estimator=="DML-IVQR-BC") max(abs(unlist(lapply(base$value$instrument,`[[`,"coefficients"))-unlist(lapply(alt$value$instrument,`[[`,"coefficients"))))
      else max(abs(base$value$delta-alt$value$delta))
    } else NA_real_,
    elapsed_baseline=base$elapsed, elapsed_alternative=alt$elapsed, stringsAsFactors=FALSE)
  cutoff <- qchisq(.95,2)
  summary$rejected_baseline <- if(base$failed) NA else base$value$W > cutoff
  summary$rejected_alternative <- if(alt$failed) NA else alt$value$W > cutoff
  summary$delta_W <- summary$W_alternative-summary$W_baseline
  summary$decision_flip <- if(both) summary$rejected_baseline != summary$rejected_alternative else NA
  saveRDS(list(task=task, baseline=base, alternative=alt, summary=summary), task$result_path)
  summary
}
