# Beavers and Botany

## Background

A study of the effects of the introduction of beavers on botanical biodiversity.
Beavers were reintroduced to the [Spains Hall Estate](https://www.spainshallestate.co.uk/nfm_beavers) in 2019
as part of a program of nature recovery and natural flood reduction.
Since then the beavers have started a family
and transformed their environment to suit their needs.
Every year a botanical survey has been conducted to monitor how the botany
of the beaver introduction site has been transformed under beaver management.

## Objectives

1. Evaluate techniques for monitoring the effects of beaver introductions.
1. Create a model to predict the timeline for the effects of beaver introductions.
1. Create an automated tool for predicting moisture and light levels from digital images.

## Data and Analysis

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#github.com/joejcollins/atlanta-shore)

To use Rstudio run `rserver` in the VSCode terminal.

Documents at <https://joejcollins.github.io/atlanta-shore/>.


## To Do

- [ ] Test data files, 2 files, 1 observation in one and 2 in the other.
- [ ] Test images, 6 images for the 3 observations.
- [ ] def raw_observation_file_finder(start_path: str) -> List[str]:
  - [ ] test to find files in the data directory.
- [ ] class RawObservationFileReader:
  - [ ] def __init__(self, file: file):
    - [ ] takes a file not a path to the file.
  - [ ] def __next__(self) -> str:
    - [ ] returns next observation up to end of species list.
- [ ] class Observation(pydantic.BaseModel):
  - [ ] validates fields
  - [ ] def csv_headers(self) -> str:
  - [ ] def to_csv(self) -> str:
- [ ] def parse_raw_observation(raw_observation: str) -> dict:
  - [ ] return a dict with the fields of the observation ready fo Pydantic.
