library(ggplot2)

ggplot(observations_year, aes(x = x.x, y = y.x, fill = wetness_estimate)) +
  geom_tile() +
  scale_fill_gradient(low = "blue", high = "red") +
  labs(x = "X Coordinate", y = "Y Coordinate", fill = "Wetness")
