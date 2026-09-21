# E1-1: Simulate F-distributed data and study its relationship with chi-square distributions

set.seed(123)

n <- 1000

df1 <- 5

df2 <- 10

# Generate two chi-square samples

chi1 <- rchisq(n, df1)

chi2 <- rchisq(n, df2)

# Build F data manually

F_data <- (chi1 / df1) / (chi2 / df2)

# Display results

cat("Mean of simulated F data:", mean(F_data), "\n")

cat("Theoretical mean of F(df1, df2):", df2 / (df2 - 2), "\n")

# Save graph as PDF

pdf("E1_1_F_Distribution.pdf", width = 8, height = 6)

hist(F_data,
     breaks = 40,
     probability = TRUE,
     col = "lightblue",
     main = "Simulated F-distribution (from Chi-square ratio)",
     xlab = "F value")

# Add theoretical F density curve

curve(df(x, df1, df2),
      add = TRUE,
      col = "red",
      lwd = 2)

# Add legend

legend("topright",
       legend = "Theoretical F density",
       col = "red",
       lwd = 2,
       bty = "n")

# Close PDF file

dev.off()






 # E1-1: Simulate F-distributed data and study its relationship with chi-square distributions

# set.seed(123)

# n <- 1000
# df1 <- 5
# df2 <- 10

# # Generate two chi-square samples
# chi1 <- rchisq(n, df1)
# chi2 <- rchisq(n, df2)

# # Build F data manually
# F_data <- (chi1 / df1) / (chi2 / df2)

# # Display results
# cat("Mean of simulated F data:", mean(F_data), "\n")
# cat("Theoretical mean of F(df1, df2):", df2 / (df2 - 2), "\n")

# # Plot in RStudio
# hist(F_data,
#      breaks = 40,
#      probability = TRUE,
#      col = "lightblue",
#      main = "Simulated F-distribution (from Chi-square ratio)",
#      xlab = "F value")

# # Add theoretical F density curve
# curve(df(x, df1, df2),
#       add = TRUE,
#       col = "red",
#       lwd = 2)

# legend("topright",
#        legend = "Theoretical F density",
#        col = "red",
#        lwd = 2,
#        bty = "n")
