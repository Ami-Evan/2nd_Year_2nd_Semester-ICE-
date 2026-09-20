# E3-4: Perform Hypothesis Testing Step-by-Step
# Using Simulated Data

set.seed(123)

sample_data <- rnorm(30, mean = 5.5, sd = 2)
alpha <- 0.05


# Step 1: Hypotheses
cat("Step 1 - Hypotheses:\n")
cat("H0: mu = 5\n")
cat("H1: mu != 5\n\n")


# Perform t-test
result <- t.test(sample_data, mu = 5)

# Step 2: Test Statistic
cat("Step 2 - Test Statistic (t):",
    result$statistic, "\n")

# Step 3: P-value
cat("Step 3 - P-value:",
    result$p.value, "\n")

# Step 4: Decision
if (result$p.value < alpha) {
  cat("Step 4 - Decision: Reject H0\n")
} else {
  cat("Step 4 - Decision: Fail to Reject H0\n")
}


# Create PDF
pdf("E3_4_Hypothesis_Test.pdf",
    width = 8,
    height = 6)


# Boxplot
boxplot(sample_data,
        col = "lightblue",
        main = "Step-by-Step Hypothesis Test Data",
        xlab = "Sample Data",
        ylab = "Value")


# H0 mean line
abline(h = 5,
       col = "red",
       lwd = 2,
       lty = 2)


# Legend
legend("topright",
       legend = "H0: mu = 5",
       col = "red",
       lty = 2,
       lwd = 2)


# Close PDF
dev.off()







 # E3-4: Perform Hypothesis Testing Step-by-Step
# # Using Simulated Data

# set.seed(123)

# sample_data <- rnorm(30, mean = 5.5, sd = 2)
# alpha <- 0.05


# # Step 1: Hypotheses
# cat("Step 1 - Hypotheses:\n")
# cat("   H0: mu = 5\n")
# cat("   H1: mu != 5\n\n")


# # Step 2: Test Statistic
# result <- t.test(sample_data, mu = 5)

# cat("Step 2 - Test Statistic (t):",
#     result$statistic, "\n")


# # Step 3: P-value
# cat("Step 3 - P-value:",
#     result$p.value, "\n")


# # Step 4: Decision
# if (result$p.value < alpha) {
#   cat("Step 4 - Decision: Reject H0\n")
# } else {
#   cat("Step 4 - Decision: Fail to Reject H0\n")
# }


# # Graph
# boxplot(sample_data,
#         col = "lightblue",
#         main = "Step-by-Step Hypothesis Test Data",
#         xlab = "Sample Data",
#         ylab = "Value")

# # H0 mean line
# abline(h = 5,
#        col = "red",
#        lwd = 2,
#        lty = 2)

# # Legend
# legend("topright",
#        legend = "H0: mu = 5",
#        col = "red",
#        lty = 2,
#        lwd = 2)
