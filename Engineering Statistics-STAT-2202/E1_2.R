# E1-2: Generate chi-square distributed data and analyze its properties

set.seed(123)

n <- 1000
df <- 5

# Generate chi-square data
chi_data <- rchisq(n, df)

# Mean and variance
cat("Sample Mean:", mean(chi_data),
    " (Theoretical:", df, ")\n")

cat("Sample Variance:", var(chi_data),
    " (Theoretical:", 2 * df, ")\n")


# Save graph as PDF
pdf("E1_2_Chi_Square_Distribution.pdf",
    width = 8, height = 6)

# Histogram
hist(chi_data,
     breaks = 30,
     probability = TRUE,
     col = "lightgreen",
     main = "Chi-square Distributed Data (df = 5)",
     xlab = "Value")

# Theoretical density curve
curve(dchisq(x, df),
      add = TRUE,
      col = "red",
      lwd = 2)

# Legend
legend("topright",
       legend = "Theoretical density",
       col = "red",
       lwd = 2,
       bty = "n")

dev.off()





# E1-2: Generate chi-square distributed data and analyze its properties

# set.seed(123)

# n <- 1000
# df <- 5

# # Generate chi-square data
# chi_data <- rchisq(n, df)

# # Mean and variance
# cat("Sample Mean:", mean(chi_data),
#     " (Theoretical:", df, ")\n")

# cat("Sample Variance:", var(chi_data),
#     " (Theoretical:", 2 * df, ")\n")

# # Histogram
# hist(chi_data,
#      breaks = 30,
#      probability = TRUE,
#      col = "lightgreen",
#      main = "Chi-square Distributed Data (df=5)",
#      xlab = "Value")

# # Theoretical density curve
# curve(dchisq(x, df),
#       add = TRUE,
#       col = "red",
#       lwd = 2)

# # Legend
# legend("topright",
#        legend = "Theoretical density",
#        col = "red",
#        lwd = 2,
#        bty = "n")