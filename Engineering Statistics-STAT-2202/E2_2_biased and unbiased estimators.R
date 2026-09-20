# E2-2: Compare biased and unbiased estimators of variance

set.seed(123)

n <- 10
N_sim <- 1000
true_var <- 4

biased <- numeric(N_sim)
unbiased <- numeric(N_sim)

for (i in 1:N_sim) {
  
  sample_data <- rnorm(n, mean = 0, sd = sqrt(true_var))
  
  # Biased estimator: divide by n
  biased[i] <- sum((sample_data - mean(sample_data))^2) / n
  
  # Unbiased estimator: divide by n-1
  unbiased[i] <- var(sample_data)
}

# Output
cat("Average biased estimator (divide by n):",
    mean(biased), "\n")

cat("Average unbiased estimator (divide by n-1):",
    mean(unbiased), "\n")

cat("True Variance:", true_var, "\n")


# Create PDF file
pdf("E2_2.pdf", width = 8, height = 6)

# Boxplot
boxplot(biased, unbiased,
        names = c("Biased (n)", "Unbiased (n-1)"),
        col = c("lightcoral", "lightgreen"),
        main = "Biased vs Unbiased Variance Estimator",
        ylab = "Estimated Variance")

# True variance line
abline(h = true_var,
       col = "blue",
       lwd = 2,
       lty = 2)

# Legend
legend("topright",
       legend = "True Variance = 4",
       col = "blue",
       lty = 2,
       lwd = 2)

# Close PDF
dev.off()
#getdw()








 # E2-2: Compare biased and unbiased estimators of variance

# set.seed(123)

# n <- 10
# N_sim <- 1000
# true_var <- 4

# biased <- numeric(N_sim)
# unbiased <- numeric(N_sim)

# for (i in 1:N_sim) {
  
#   sample_data <- rnorm(n, mean = 0, sd = sqrt(true_var))
  
#   # Biased estimator: divide by n
#   biased[i] <- sum((sample_data - mean(sample_data))^2) / n
  
#   # Unbiased estimator: divide by n-1
#   unbiased[i] <- var(sample_data)
# }

# # Output
# cat("Average biased estimator (divide by n):",
#     mean(biased), "\n")

# cat("Average unbiased estimator (divide by n-1):",
#     mean(unbiased), "\n")

# cat("True Variance:", true_var, "\n")


# # Graph
# boxplot(biased, unbiased,
#         names = c("Biased (n)", "Unbiased (n-1)"),
#         col = c("lightcoral", "lightgreen"),
#         main = "Biased vs Unbiased Variance Estimator",
#         ylab = "Estimated Variance")

# # True variance line
# abline(h = true_var,
#        col = "blue",
#        lwd = 2,
#        lty = 2)

# # Legend
# legend("topright",
#        legend = "True Variance = 4",
#        col = "blue",
#        lty = 2,
#        lwd = 2)
