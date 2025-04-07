suppressPackageStartupMessages(library(leaflet))
suppressPackageStartupMessages(library(readr))
sample_points_path <- paste0(
  "data/raw/spains-hall-waypoints-regular-30m",
  "-with-name-edited.csv"
)

col_types <- cols(
  sample_point_id = col_character(),
  lat = col_double(),
  lon = col_double(),
  eastings = col_integer(),
  northings = col_integer(),
  grid_ref = col_character()
)


sample_points <- read_csv(sample_points_path, col_types = col_types)


# Create a leaflet map
m <- leaflet()

# Add map tiles
m <- addProviderTiles(m, "OpenStreetMap.Mapnik")

# Add markers for each point
for (i in seq_len(nrow(sample_points))) {
  m <- addMarkers(m, lng = sample_points$lon[i], lat = sample_points$lat[i])
}

# Display the map
m
