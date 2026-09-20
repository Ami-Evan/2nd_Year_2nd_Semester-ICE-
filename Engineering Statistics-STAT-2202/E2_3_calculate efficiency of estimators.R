# E2-3: Calculate efficiency of estimators
# Mean vs Median

set.seed(123)

n <- 30
N_sim <- 1000
mu <- 5

means <- numeric(N_sim)
medians <- numeric(N_sim)

for (i in 1:N_sim) {
  
  sample_data <- rnorm(n, mean = mu, sd = 2)
  
  means[i] <- mean(sample_data)
  medians[i] <- median(sample_data)
}

# Output
cat("Variance of Sample Mean:",
    var(means), "\n")

cat("Variance of Sample Median:",
    var(medians), "\n")

cat("Relative Efficiency (Median vs Mean):",
    var(medians) / var(means), "\n")

cat("(Value > 1 means Mean is more efficient than Median)\n")


# Create PDF
pdf("E2_3.pdf", width = 8, height = 6)

# Boxplot
boxplot(means, medians,
        names = c("Mean", "Median"),
        col = c("skyblue", "orange"),
        main = "Efficiency Comparison: Mean vs Median",
        ylab = "Estimator Values")

# True mean line
abline(h = mu,
       col = "red",
       lwd = 2,
       lty = 2)

# Legend
legend("topright",
       legend = "True Mean = 5",
       col = "red",
       lty = 2,
       lwd = 2)

# Close PDF
dev.off()






# E2-3: Calculate efficiency of estimators
# # Mean vs Median

# set.seed(123)

# n <- 30
# N_sim <- 1000
# mu <- 5

# means <- numeric(N_sim)
# medians <- numeric(N_sim)

# for (i in 1:N_sim) {
  
#   sample_data <- rnorm(n, mean = mu, sd = 2)
  
#   means[i] <- mean(sample_data)
#   medians[i] <- median(sample_data)
# }

# # Output
# cat("Variance of Sample Mean:", var(means), "\n")

# cat("Variance of Sample Median:", var(medians), "\n")

# cat("Relative Efficiency (Median vs Mean):",
#     var(medians) / var(means), "\n")

# cat("(Value > 1 means Mean is more efficient than Median)\n")


# # Graph in RStudio
# boxplot(means, medians,
#         names = c("Mean", "Median"),
#         col = c("skyblue", "orange"),
#         main = "Efficiency Comparison: Mean vs Median",
#         ylab = "Estimator Values")

# # True mean line
# abline(h = mu,
#        col = "red",
#        lwd = 2,
#        lty = 2)

# # Legend
# legend("topright",
#        legend = "True Mean = 5",
#        col = "red",
#        lty = 2,
#        lwd = 2)
