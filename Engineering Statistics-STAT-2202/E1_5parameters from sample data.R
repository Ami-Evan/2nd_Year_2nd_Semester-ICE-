# E1-5: Estimate population parameters from sample data

set.seed(123)

n <- 30

# Generate sample data
sample_data <- rnorm(n, mean = 5, sd = 2)

# Calculate sample mean and variance
sample_mean <- mean(sample_data)
sample_var <- var(sample_data)

# 95% Confidence Interval for Mean
ci_mean <- t.test(sample_data)$conf.int

# 95% Confidence Interval for Variance
ci_var <- c(
  (n - 1) * sample_var / qchisq(0.975, n - 1),
  (n - 1) * sample_var / qchisq(0.025, n - 1)
)

# Display results
cat("Sample Mean:", sample_mean, "\n")
cat("Sample Variance:", sample_var, "\n")
cat("95% CI for Mean:", ci_mean, "\n")
cat("95% CI for Variance:", ci_var, "\n")


# Create PDF file
pdf("E1_5.pdf", width = 7, height = 5)

# Histogram
hist(sample_data,
     breaks = 10,
     col = "lightblue",
     main = "Sample Data",
     xlab = "Value")

# Show sample mean
abline(v = sample_mean,
       col = "red",
       lwd = 2)

# Close PDF
dev.off()



# # E1-5: Estimate population parameters from sample data

# set.seed(123)

# n <- 30

# # Generate sample data
# sample_data <- rnorm(n, mean = 5, sd = 2)

# # Calculate sample mean and variance
# sample_mean <- mean(sample_data)
# sample_var <- var(sample_data)

# # 95% CI for Mean
# ci_mean <- t.test(sample_data)$conf.int

# # 95% CI for Variance
# ci_var <- c(
#   (n - 1) * sample_var / qchisq(0.975, n - 1),
#   (n - 1) * sample_var / qchisq(0.025, n - 1)
# )

# # Display results
# cat("Sample Mean:", sample_mean, "\n")
# cat("Sample Variance:", sample_var, "\n")
# cat("95% CI for Mean:", ci_mean, "\n")
# cat("95% CI for Variance:", ci_var, "\n")


# # Histogram
# hist(sample_data,
#      breaks = 10,
#      probability = TRUE,
#      col = "lightblue",
#      main = "Sample Data with Normal Curve",
#      xlab = "Value")

# # Theoretical Normal Curve
# curve(dnorm(x, mean = 5, sd = 2),
#       add = TRUE,
#       col = "red",
#       lwd = 2)

# # Sample Mean Line
# abline(v = sample_mean,
#        col = "blue",
#        lwd = 2)

# # Legend
# legend("topright",
#        legend = c("Normal Curve", "Sample Mean"),
#        col = c("red", "blue"),
#        lwd = 2)