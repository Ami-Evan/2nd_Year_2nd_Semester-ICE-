# E1-4

set.seed(123)

n <- 20
N_sim <- 1000

medians <- numeric(N_sim)
ranges <- numeric(N_sim)

for (i in 1:N_sim) {
  
  sample_data <- rnorm(n, mean = 50, sd = 10)
  
  medians[i] <- median(sample_data)
  ranges[i] <- max(sample_data) - min(sample_data)
}

cat("Mean of sample medians:", mean(medians), "\n")
cat("Mean of sample ranges:", mean(ranges), "\n")


# Create PDF
pdf("E1_4.pdf", width = 10, height = 5)

# Two graphs side by side
par(mfrow = c(1, 2))

hist(medians,
     breaks = 20,
     col = "lightblue",
     main = "Distribution of Sample Medians",
     xlab = "Median")

hist(ranges,
     breaks = 20,
     col = "lightpink",
     main = "Distribution of Sample Ranges",
     xlab = "Range")

# Close PDF
dev.off()









# # E1-4: Generate samples from a population and study
# # the distribution of medians and ranges

# set.seed(123)

# n <- 20
# N_sim <- 1000

# medians <- numeric(N_sim)
# ranges <- numeric(N_sim)

# for (i in 1:N_sim) {

#   sample_data <- rnorm(n, mean = 50, sd = 10)

#   medians[i] <- median(sample_data)

#   ranges[i] <- max(sample_data) - min(sample_data)
# }

# # Display results
# cat("Mean of sample medians:", mean(medians), "\n")
# cat("Mean of sample ranges:", mean(ranges), "\n")


# # -------- Graph --------

# par(mfrow = c(1, 2))

# # Distribution of sample medians
# hist(medians,
#      col = "lightblue",
#      main = "Distribution of Sample Medians",
#      xlab = "Median")


# # Distribution of sample ranges
# hist(ranges,
#      col = "lightpink",
#      main = "Distribution of Sample Ranges",
#      xlab = "Range")
