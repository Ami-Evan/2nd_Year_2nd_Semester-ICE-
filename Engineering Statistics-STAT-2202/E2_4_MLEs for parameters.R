# E2-4: MLE for Binomial, Poisson and Normal Distributions

set.seed(123)

# -------------------------------
# Binomial MLE
# -------------------------------

bin_data <- rbinom(1000, size = 10, prob = 0.3)

p_hat <- mean(bin_data) / 10

cat("Binomial MLE (p_hat):", p_hat,
    " (True p = 0.3)\n")


# -------------------------------
# Poisson MLE
# -------------------------------

pois_data <- rpois(1000, lambda = 4)

lambda_hat <- mean(pois_data)

cat("Poisson MLE (lambda_hat):", lambda_hat,
    " (True lambda = 4)\n")


# -------------------------------
# Normal MLE
# -------------------------------

norm_data <- rnorm(1000, mean = 10, sd = 3)

mu_hat <- mean(norm_data)

var_hat <- mean((norm_data - mu_hat)^2)

cat("Normal MLE (mu_hat):", mu_hat,
    " (True mu = 10)\n")

cat("Normal MLE (var_hat):", var_hat,
    " (True var = 9)\n")


# -------------------------------
# Create PDF
# -------------------------------

pdf("E2_4.pdf", width = 12, height = 5)

# Divide the page into 3 graphs
par(mfrow = c(1, 3))

# Binomial graph
hist(bin_data,
     col = "lightblue",
     main = "Binomial Data",
     xlab = "Value")

# Poisson graph
hist(pois_data,
     col = "lightgreen",
     main = "Poisson Data",
     xlab = "Value")

# Normal graph
hist(norm_data,
     col = "lightpink",
     main = "Normal Data",
     xlab = "Value")

# Close PDF
dev.off()









# E2-4: MLE for Binomial, Poisson and Normal Distributions

# set.seed(123)

# # Binomial MLE
# bin_data <- rbinom(1000, size = 10, prob = 0.3)

# p_hat <- mean(bin_data) / 10

# cat("Binomial MLE (p_hat):", p_hat,
#     " (True p = 0.3)\n")


# # Poisson MLE
# pois_data <- rpois(1000, lambda = 4)

# lambda_hat <- mean(pois_data)

# cat("Poisson MLE (lambda_hat):", lambda_hat,
#     " (True lambda = 4)\n")


# # Normal MLE
# norm_data <- rnorm(1000, mean = 10, sd = 3)

# mu_hat <- mean(norm_data)

# var_hat <- mean((norm_data - mu_hat)^2)

# cat("Normal MLE (mu_hat):", mu_hat,
#     " (True mu = 10)\n")

# cat("Normal MLE (var_hat):", var_hat,
#     " (True var = 9)\n")


# # Show 3 graphs in RStudio
# par(mfrow = c(1, 3))

# # Binomial
# hist(bin_data,
#      col = "lightblue",
#      main = "Binomial Data",
#      xlab = "Value")

# # Poisson
# hist(pois_data,
#      col = "lightgreen",
#      main = "Poisson Data",
#      xlab = "Value")

# # Normal
# hist(norm_data,
#      col = "lightpink",
#      main = "Normal Data",
#      xlab = "Value")

# # Reset graph layout
# par(mfrow = c(1, 1))
