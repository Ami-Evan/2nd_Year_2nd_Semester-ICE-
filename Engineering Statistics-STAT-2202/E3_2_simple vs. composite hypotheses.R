# E3-2: Best Critical Region
# H0: mu = 0 vs H1: mu = 2

alpha <- 0.05

# Critical value
crit_value <- qnorm(1 - alpha, mean = 0, sd = 1)

cat("H0: mu = 0 vs H1: mu = 2\n")
cat("Critical value =", crit_value, "\n")
cat("Reject H0 if sample mean >", crit_value, "\n")


# x values
x <- seq(-4, 6, length.out = 300)

# Create PDF
pdf("E3_2_Best_Critical_Region.pdf", width = 8, height = 6)

# H0 distribution
plot(x, dnorm(x, mean = 0, sd = 1),
     type = "l",
     col = "blue",
     lwd = 2,
     main = "Best Critical Region",
     xlab = "Sample Mean",
     ylab = "Density")

# H1 distribution
lines(x, dnorm(x, mean = 2, sd = 1),
      col = "red",
      lwd = 2)

# Critical value
abline(v = crit_value,
       col = "darkgreen",
       lwd = 2,
       lty = 2)

# Legend
legend("topright",
       legend = c("H0: mu = 0",
                  "H1: mu = 2",
                  "Critical value"),
       col = c("blue", "red", "darkgreen"),
       lty = c(1, 1, 2),
       lwd = 2)

# Close PDF
dev.off()





 # E3-2: Best Critical Region
# # H0: mu = 0 vs H1: mu = 2
# # Normal distribution, sigma = 1

# alpha <- 0.05

# # Critical value
# crit_value <- qnorm(1 - alpha, mean = 0, sd = 1)

# cat("H0: mu = 0 vs H1: mu = 2\n")
# cat("Critical value =", crit_value, "\n")
# cat("Reject H0 if sample mean >", crit_value, "\n")


# # x values
# x <- seq(-4, 6, length.out = 300)

# # H0 distribution
# y0 <- dnorm(x, mean = 0, sd = 1)

# # H1 distribution
# y1 <- dnorm(x, mean = 2, sd = 1)

# # Plot H0
# plot(x, y0,
#      type = "l",
#      lwd = 2,
#      col = "blue",
#      main = "Best Critical Region",
#      xlab = "Sample Mean",
#      ylab = "Density")

# # Add H1
# lines(x, y1,
#       col = "red",
#       lwd = 2)

# # Critical value
# abline(v = crit_value,
#        col = "darkgreen",
#        lwd = 2,
#        lty = 2)

# # Legend
# legend("topright",
#        legend = c("H0: mu = 0",
#                   "H1: mu = 2",
#                   "Critical value"),
#        col = c("blue", "red", "darkgreen"),
#        lty = c(1, 1, 2),
#        lwd = 2)
