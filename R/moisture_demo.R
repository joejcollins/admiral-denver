suppressPackageStartupMessages(library(ggplot2))

# Generate example data
moisture <- expand.grid(x = 1:10, y = 1:10)
moisture$moisture <- runif(100, min = 0, max = 1)

# Plot the grid of moisture values
ggplot(moisture, aes(x, y, fill = moisture)) +
  geom_tile() +
  scale_fill_gradient(low = "white", high = "blue")


ggplot(moisture, aes(x = x, y = y)) +
  geom_point(aes(size = moisture)) +
  scale_size_continuous(range = c(3, 7))
