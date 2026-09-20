# E3-3: Simulate Type I and Type II Errors

set.seed(123)

n <- 30
N_sim <- 1000
alpha <- 0.05

type1_count <- 0
type2_count <- 0

for (i in 1:N_sim) {

  # Case 1: H0 is actually true
  sample_h0 <- rnorm(n, mean = 5, sd = 2)

  p_h0 <- t.test(sample_h0, mu = 5)$p.value

  if (p_h0 < alpha) {
    type1_count <- type1_count + 1
  }


  # Case 2: H1 is actually true
  sample_h1 <- rnorm(n, mean = 6, sd = 2)

  p_h1 <- t.test(sample_h1, mu = 5)$p.value

  if (p_h1 >= alpha) {
    type2_count <- type2_count + 1
  }
}


# Calculate error rates
type1_rate <- type1_count / N_sim
type2_rate <- type2_count / N_sim

cat("Type I Error Rate:", type1_rate, "\n")
cat("Type II Error Rate:", type2_rate, "\n")


# Create PDF
pdf("E3_3_Type1_Type2_Error.pdf", width = 8, height = 6)

# Bar graph
barplot(c(type1_rate, type2_rate),
        names.arg = c("Type I Error", "Type II Error"),
        col = c("red", "orange"),
        main = "Type I and Type II Error Rates",
        xlab = "Error Type",
        ylab = "Error Rate",
        ylim = c(0, max(type1_rate, type2_rate) + 0.05))

# Add values above bars
text(x = c(0.7, 1.9),
     y = c(type1_rate, type2_rate),
     labels = round(c(type1_rate, type2_rate), 3),
     pos = 3)

# Close PDF
dev.off()





 # E3-3: Simulate Type I and Type II Errors

# set.seed(123)

# n <- 30
# N_sim <- 1000
# alpha <- 0.05

# type1_count <- 0
# type2_count <- 0

# for (i in 1:N_sim) {

#   # Case 1: H0 is actually true
#   sample_h0 <- rnorm(n, mean = 5, sd = 2)

#   p_h0 <- t.test(sample_h0, mu = 5)$p.value

#   if (p_h0 < alpha) {
#     type1_count <- type1_count + 1
#   }


#   # Case 2: H1 is actually true
#   sample_h1 <- rnorm(n, mean = 6, sd = 2)

#   p_h1 <- t.test(sample_h1, mu = 5)$p.value

#   if (p_h1 >= alpha) {
#     type2_count <- type2_count + 1
#   }
# }


# # Calculate error rates
# type1_rate <- type1_count / N_sim
# type2_rate <- type2_count / N_sim

# cat("Type I Error Rate:", type1_rate, "\n")
# cat("Type II Error Rate:", type2_rate, "\n")


# # Bar graph
# barplot(c(type1_rate, type2_rate),
#         names.arg = c("Type I Error", "Type II Error"),
#         col = c("red", "orange"),
#         main = "Type I and Type II Error Rates",
#         xlab = "Error Type",
#         ylab = "Error Rate",
#         ylim = c(0, max(type1_rate, type2_rate) + 0.05))
