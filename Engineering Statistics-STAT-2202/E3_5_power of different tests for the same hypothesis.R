# E3-5: Compare the power of t-test vs z-test

set.seed(123)

n <- 30
alpha <- 0.05
true_means <- seq(5, 8, by = 0.5)
N_sim <- 500

power_t <- numeric(length(true_means))
power_z <- numeric(length(true_means))

for (j in seq_along(true_means)) {
  
  reject_t <- 0
  reject_z <- 0
  
  for (i in 1:N_sim) {
    
    sample_data <- rnorm(n, mean = true_means[j], sd = 2)
    
    # t-test
    if (t.test(sample_data, mu = 5)$p.value < alpha) {
      reject_t <- reject_t + 1
    }
    
    # z-test
    z <- (mean(sample_data) - 5) / (2 / sqrt(n))
    p_z <- 2 * (1 - pnorm(abs(z)))
    
    if (p_z < alpha) {
      reject_z <- reject_z + 1
    }
  }
  
  power_t[j] <- reject_t / N_sim
  power_z[j] <- reject_z / N_sim
}

# Display results
cat("True Means:", true_means, "\n")
cat("Power (t-test):", power_t, "\n")
cat("Power (z-test):", power_z, "\n")


# Save graph as PDF
pdf("E3_5_Power_Comparison.pdf", width = 8, height = 6)

plot(true_means, power_t,
     type = "b",
     col = "blue",
     lwd = 2,
     ylim = c(0, 1),
     main = "Power Comparison: t-test vs z-test",
     xlab = "True Mean",
     ylab = "Power")

lines(true_means, power_z,
      type = "b",
      col = "red",
      lwd = 2)

legend("bottomright",
       legend = c("t-test", "z-test"),
       col = c("blue", "red"),
       lwd = 2)

dev.off()




# E3-5: Compare the power of different tests (t-test vs z-test)

# set.seed(123)

# n <- 30
# alpha <- 0.05
# true_means <- seq(5, 8, by = 0.5)
# N_sim <- 500

# power_t <- numeric(length(true_means))
# power_z <- numeric(length(true_means))

# for (j in seq_along(true_means)) {
  
#   reject_t <- 0
#   reject_z <- 0
  
#   for (i in 1:N_sim) {
    
#     sample_data <- rnorm(n, mean = true_means[j], sd = 2)
    
#     # t-test
#     if (t.test(sample_data, mu = 5)$p.value < alpha) {
#       reject_t <- reject_t + 1
#     }
    
#     # z-test
#     z <- (mean(sample_data) - 5) / (2 / sqrt(n))
#     p_z <- 2 * (1 - pnorm(abs(z)))
    
#     if (p_z < alpha) {
#       reject_z <- reject_z + 1
#     }
#   }
  
#   power_t[j] <- reject_t / N_sim
#   power_z[j] <- reject_z / N_sim
# }

# # Display results
# cat("True Means:", true_means, "\n")
# cat("Power (t-test):", power_t, "\n")
# cat("Power (z-test):", power_z, "\n")


# # Graph for RStudio Plots pane
# plot(true_means, power_t,
#      type = "b",
#      col = "blue",
#      lwd = 2,
#      ylim = c(0, 1),
#      main = "Power Comparison: t-test vs z-test",
#      xlab = "True Mean",
#      ylab = "Power")

# lines(true_means, power_z,
#       type = "b",
#       col = "red",
#       lwd = 2)

# legend("bottomright",
#        legend = c("t-test", "z-test"),
#        col = c("blue", "red"),
#        lwd = 2)
