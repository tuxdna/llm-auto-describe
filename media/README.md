# Dataset Description

## Overview
The dataset consists of 2,652 entries across 8 features. It includes information related to various types of media, particularly focusing on reviews or ratings for fiction and movies in different languages.

## Shape of Data
- **Number of Rows:** 2652
- **Number of Columns:** 8

## Data Types
The columns in the dataset have the following data types:
- **date:** object (string representation of date)
- **language:** object (categorical representation of language)
- **type:** object (categorical representation of media type)
- **title:** object (string representation of the media title)
- **by:** object (string representation of the creators or contributors)
- **overall:** int64 (integer representation of overall rating)
- **quality:** int64 (integer representation of quality rating)
- **repeatability:** int64 (integer representation of repeatability rating)

## Null Counts
The dataset has some missing values in the following features:
- **date:** 99 missing entries
- **language:** 0 missing entries
- **type:** 0 missing entries
- **title:** 0 missing entries
- **by:** 262 missing entries
- **overall:** 0 missing entries
- **quality:** 0 missing entries
- **repeatability:** 0 missing entries

## Descriptive Statistics of Numeric Features
The following statistics summarize the numeric features:
- **overall:**
  - Count: 2652
  - Mean: 3.05
  - Standard Deviation: 0.76
  - Minimum: 1
  - 25th Percentile: 3
  - Median (50th Percentile): 3
  - 75th Percentile: 3
  - Maximum: 5
  
- **quality:**
  - Count: 2652
  - Mean: 3.21
  - Standard Deviation: 0.80
  - Minimum: 1
  - 25th Percentile: 3
  - Median (50th Percentile): 3
  - 75th Percentile: 4
  - Maximum: 5
  
- **repeatability:**
  - Count: 2652
  - Mean: 1.49
  - Standard Deviation: 0.60
  - Minimum: 1
  - 25th Percentile: 1
  - Median (50th Percentile): 1
  - 75th Percentile: 2
  - Maximum: 3

## Sample Data
Here are ten samples from the dataset:

|      | date      | language   | type    | title                         | by                             |   overall |   quality |   repeatability |
|-----:|:----------|:-----------|:--------|:------------------------------|:-------------------------------|----------:|----------:|----------------:|
| 1796 | 11-Nov-08 | English    | fiction | The Alchemyst                 | Michael Scott                  |         3 |         3 |               2 |
| 2442 | 28-Nov-05 | English    | movie   | The Towering Inferno          | Steve McQueen, Paul Newman     |         4 |         3 |               2 |
| 1335 | 02-Jul-13 | English    | movie   | Taken 2                       | Liam Neeson                    |         3 |         3 |               2 |
|  719 | 26-Jan-19 | Hindi      | movie   | Andhadhun                     | Ayushmann Khurrana, Tabu       |         4 |         4 |               1 |
| 1811 | 14-Oct-08 | Tamil      | movie   | Missiamma                     | Gemini, Savithri               |         4 |         4 |               2 |
| 1286 | 29-Nov-13 | Tamil      | movie   | Varuthapadatha Valibar Sangam | Sivakarthikeyan, Sathyaraj     |         2 |         2 |               2 |
| 1528 | 05-Oct-10 | English    | fiction | The Sorceress                 | Michael Scott                  |         2 |         2 |               2 |
| 2377 | 06-Feb-06 | English    | movie   | Training Day                  | Denzel Washington, Ben Affleck |         4 |         4 |               1 |
| 1382 | 31-May-12 | Tamil      | movie   | Aaru                          | Surya, Trisha                  |         3 |         3 |               2 |
| 1511 | 02-Jan-11 | Tamil      | movie   | Uthama Puthiran               | Dhanush, Genelia               |         3 |         3 |               2 |

# Histogram of features: ['overall', 'quality', 'repeatability']

Let us explore some features below



## Plot of feature: overall

![overall.plot.png](overall.plot.png)



## Plot of feature: quality

![quality.plot.png](quality.plot.png)



## Plot of feature: repeatability

![repeatability.plot.png](repeatability.plot.png)

