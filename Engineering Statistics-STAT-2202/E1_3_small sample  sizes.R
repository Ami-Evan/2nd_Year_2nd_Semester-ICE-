df <- 5
x <- seq(-4, 4, length.out = 200)

# PDF file open
pdf("E1_3.pdf", width = 7, height = 5)

# Normal distribution
plot(x, dnorm(x),
     type = "l",
     col = "blue",
     lwd = 2,
     main = "t-distribution vs Normal Distribution (df=5)",
     xlab = "Value",
     ylab = "Density")

# t-distribution
lines(x, dt(x, df),
      col = "red",
      lwd = 2)

# Legend
legend("topright",
       legend = c("Normal", "t (df=5)"),
       col = c("blue", "red"),
       lwd = 2)

# Save and close PDF
dev.off()





# # E1-3: Compare t-distribution with normal distribution for small sample sizes

# df <- 5

# x <- seq(-4, 4, length = 200)

# cat("Comparing Normal(0,1) with t-distribution (df =", df, ")\n")
# cat("t-distribution has heavier tails than Normal for small df.\n")

# # Normal distribution
# plot(x, dnorm(x),
#      type = "l",
#      col = "blue",
#      lwd = 2,
#      main = "t-distribution vs Normal Distribution (small df)",
#      xlab = "Value",
#      ylab = "Density")

# # t-distribution
# lines(x, dt(x, df),
#       col = "red",
#       lwd = 2)

# # Legend
# legend("topright",
#        legend = c("Normal", "t (df=5)"),
#        col = c("blue", "red"),
#        lwd = 2)



