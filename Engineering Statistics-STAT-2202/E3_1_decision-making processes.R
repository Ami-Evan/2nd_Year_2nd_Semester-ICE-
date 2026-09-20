# E3-1: Hypothesis Testing

set.seed(123)

sample_data <- rnorm(30, mean = 5.5, sd = 2)

# H0: mu = 5
# H1: mu != 5

result <- t.test(sample_data, mu = 5)

cat("Test Statistic:", result$statistic, "\n")
cat("P-value:", result$p.value, "\n")

if (result$p.value < 0.05) {
  cat("Decision: Reject Null Hypothesis\n")
} else {
  cat("Decision: Fail to Reject Null Hypothesis\n")
}


# Save graph as PDF
pdf("E3_1.pdf", width = 8, height = 6)

hist(sample_data,
     col = "lightblue",
     main = "Sample Data for Hypothesis Test",
     xlab = "Value",
     ylab = "Frequency")

# H0 mean = 5
abline(v = 5,
       col = "red",
       lwd = 2,
       lty = 2)

# Sample mean
abline(v = mean(sample_data),
       col = "blue",
       lwd = 2)

legend("topright",
       legend = c("H0: mu = 5", "Sample Mean"),
       col = c("red", "blue"),
       lty = c(2, 1),
       lwd = 2)

dev.off()






 # E3-1: Simulate decision-making process using hypothesis testing

# set.seed(123)

# sample_data <- rnorm(30, mean = 5.5, sd = 2)

# # H0: mu = 5
# # H1: mu != 5

# result <- t.test(sample_data, mu = 5)

# # Test results
# cat("Test Statistic:", result$statistic, "\n")
# cat("P-value:", result$p.value, "\n")

# # Decision
# if (result$p.value < 0.05) {
#   cat("Decision: Reject Null Hypothesis\n")
# } else {
#   cat("Decision: Fail to Reject Null Hypothesis\n")
# }


# # Graph in RStudio
# hist(sample_data,
#      col = "lightblue",
#      main = "Sample Data for Hypothesis Test",
#      xlab = "Value",
#      ylab = "Frequency")

# # H0 mean = 5
# abline(v = 5,
#        col = "red",
#        lwd = 2,
#        lty = 2)

# # Sample mean
# abline(v = mean(sample_data),
#        col = "blue",
#        lwd = 2)

# # Legend
# legend("topright",
#        legend = c("H0: mu = 5", "Sample Mean"),
#        col = c("red", "blue"),
#        lty = c(2, 1),
#        lwd = 2)
