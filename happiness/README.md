# Detailed Description of the Dataset

## Overview
The dataset consists of 2,363 rows and 11 columns, capturing various socio-economic and psychological indicators across different countries and years. Each row represents a unique combination of a country and a specific year, providing insights into the quality of life, economic factors, and social dynamics.

## Data Types
The dataset includes the following features with their respective data types:
- **Country name**: object (string)
- **year**: int64 (integer)
- **Life Ladder**: float64 (numeric)
- **Log GDP per capita**: float64 (numeric)
- **Social support**: float64 (numeric)
- **Healthy life expectancy at birth**: float64 (numeric)
- **Freedom to make life choices**: float64 (numeric)
- **Generosity**: float64 (numeric)
- **Perceptions of corruption**: float64 (numeric)
- **Positive affect**: float64 (numeric)
- **Negative affect**: float64 (numeric)

## Missing Values
The dataset contains missing values in several features, as detailed below:
- **Log GDP per capita**: 28 missing values
- **Social support**: 13 missing values
- **Healthy life expectancy at birth**: 63 missing values
- **Freedom to make life choices**: 36 missing values
- **Generosity**: 81 missing values
- **Perceptions of corruption**: 125 missing values
- **Positive affect**: 24 missing values
- **Negative affect**: 16 missing values

All other features (Country name and year) have no missing values.

## Descriptive Statistics
The dataset provides the following summary statistics for the numeric features:

| Feature                                   | Count   | Mean       | Std Dev   | Min       | 25%       | 50%       | 75%       | Max       |
|-------------------------------------------|---------|------------|-----------|-----------|-----------|-----------|-----------|-----------|
| year                                      | 2363    | 2014.76    | 5.06      | 2005      | 2011      | 2015      | 2019      | 2023      |
| Life Ladder                               | 2363    | 5.48       | 1.13      | 1.28      | 4.65      | 5.45      | 6.32      | 8.02      |
| Log GDP per capita                        | 2335    | 9.40       | 1.15      | 5.53      | 8.51      | 9.50      | 10.39     | 11.68     |
| Social support                            | 2350    | 0.81       | 0.12      | 0.23      | 0.74      | 0.83      | 0.90      | 0.99      |
| Healthy life expectancy at birth          | 2300    | 63.40      | 6.84      | 6.72      | 59.20     | 65.10     | 68.55     | 74.60     |
| Freedom to make life choices              | 2327    | 0.75       | 0.14      | 0.23      | 0.66      | 0.77      | 0.86      | 0.99      |
| Generosity                                | 2282    | 0.00       | 0.16      | -0.34     | -0.11     | -0.02     | 0.09      | 0.70      |
| Perceptions of corruption                 | 2238    | 0.74       | 0.18      | 0.04      | 0.69      | 0.80      | 0.87      | 0.98      |
| Positive affect                           | 2339    | 0.65       | 0.11      | 0.18      | 0.57      | 0.66      | 0.74      | 0.88      |
| Negative affect                           | 2347    | 0.27       | 0.09      | 0.08      | 0.21      | 0.26      | 0.33      | 0.71      |

## Sample Data
Below are ten samples from the dataset:

|      | Country name   |   year |   Life Ladder |   Log GDP per capita |   Social support |   Healthy life expectancy at birth |   Freedom to make life choices |   Generosity |   Perceptions of corruption |   Positive affect |   Negative affect |
|-----:|:---------------|-------:|--------------:|---------------------:|-----------------:|-----------------------------------:|-------------------------------:|-------------:|----------------------------:|------------------:|------------------|
| 1300 | Mali           |   2012 |         4.313 |                7.572 |            0.823 |                             51.98  |                          0.704 |       -0.091 |                       0.787 |             0.647 |             0.109 |
|  704 | Gabon          |   2016 |         4.832 |                9.601 |            0.78  |                             56.625 |                          0.699 |       -0.207 |                       0.817 |             0.625 |             0.432 |
| 2309 | Vietnam        |   2019 |         5.467 |                9.235 |            0.848 |                             65.3   |                          0.952 |       -0.148 |                       0.788 |             0.658 |             0.186 |
|  787 | Greece         |   2023 |         5.796 |               10.387 |            0.818 |                             71.4   |                          0.589 |       -0.223 |                       0.805 |             0.608 |             0.311 |
| 1440 | Mozambique     |   2021 |         5.178 |                7.112 |            0.664 |                             51.3   |                          0.838 |        0.042 |                       0.627 |             0.576 |             0.383 |
|  977 | Israel         |   2012 |         7.111 |               10.487 |            0.903 |                             71.56  |                          0.681 |        0.147 |                       0.862 |             0.611 |             0.319 |
|  546 | Denmark        |   2013 |         7.589 |               10.849 |            0.965 |                             70.06  |                          0.92  |        0.209 |                       0.17  |             0.826 |             0.195 |
| 1789 | Senegal        |   2008 |         4.683 |                7.941 |            0.756 |                             56.1   |                          0.612 |       -0.037 |                       0.879 |             0.669 |             0.252 |
| 1850 | Singapore      |   2022 |         6.333 |               11.59  |            0.852 |                             73.9   |                          0.873 |        0.088 |                     nan     |             0.688 |             0.209 |
| 2144 | Türkiye        |   2013 |         4.888 |               10.082 |            0.795 |                             67.38  |                          0.541 |       -0.235 |                       0.698 |             0.551 |             0.392 |

## Summary
This dataset provides a comprehensive overview of various factors affecting the quality of life across different countries and years. It captures economic, social, and psychological dimensions, making it a valuable resource for analysis in social sciences, economics, and public policy.

# Histogram of features: ['year', 'Life Ladder', 'Log GDP per capita', 'Social support', 'Healthy life expectancy at birth', 'Freedom to make life choices', 'Generosity', 'Perceptions of corruption', 'Positive affect', 'Negative affect']

Let us explore some of these features below



## Plot of feature: year

![year.plot.png](year.plot.png)



## Plot of feature: Life Ladder

![Life Ladder.plot.png](Life Ladder.plot.png)

