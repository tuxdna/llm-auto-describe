# Detailed Description of the Dataset

## Overview
The dataset consists of 2,652 entries and 8 features. It appears to be a collection of reviews or ratings for various types of media, including movies and TV series, in multiple languages. The dataset includes both qualitative and quantitative attributes.

## Features

1. **date** (object):
   - Represents the date when the entry was made.
   - Contains 99 null values.

2. **language** (object):
   - Specifies the language of the media.
   - No null values.

3. **type** (object):
   - Indicates the type of media (e.g., movie, TV series, non-fiction).
   - No null values.

4. **title** (object):
   - The title of the media.
   - No null values.

5. **by** (object):
   - Represents the creators or actors involved in the media.
   - Contains 262 null values, indicating that a significant number of entries lack this information.

6. **overall** (int64):
   - A numerical rating given to the media on a scale (1 to 5).
   - No null values.
   - Descriptive statistics:
     - Mean: 3.05
     - Standard Deviation: 0.76
     - Minimum: 1
     - Maximum: 5

7. **quality** (int64):
   - A numerical rating that likely reflects the quality of the media, also on a scale (1 to 5).
   - No null values.
   - Descriptive statistics:
     - Mean: 3.21
     - Standard Deviation: 0.80
     - Minimum: 1
     - Maximum: 5

8. **repeatability** (int64):
   - A numerical rating that may indicate how likely the reviewer is to recommend the media for repeated viewing.
   - No null values.
   - Descriptive statistics:
     - Mean: 1.49
     - Standard Deviation: 0.60
     - Minimum: 1
     - Maximum: 3

## Null Counts
- **date**: 99 null values
- **language**: 0 null values
- **type**: 0 null values
- **title**: 0 null values
- **by**: 262 null values
- **overall**: 0 null values
- **quality**: 0 null values
- **repeatability**: 0 null values

## Descriptive Statistics of Numeric Features
- **Overall Ratings**: 
  - Mean: 3.05, with a standard deviation of 0.76.
  - Ratings are skewed towards 3, with 75% of the ratings being 3 or lower.
  
- **Quality Ratings**: 
  - Mean: 3.21, indicating a generally positive perception of quality among the entries.
  - Similarly skewed, with a majority rating of 3 or lower.
  
- **Repeatability Ratings**: 
  - Mean: 1.49, suggesting that repeatability is generally rated lower compared to overall and quality.
  - All ratings are at least 1, indicating some level of agreement on repeatability.

## Sample Entries
The dataset contains various entries showcasing different languages, media types, and ratings. Some examples include:
- "Asura" (Telugu movie) rated 2 overall and 3 in quality.
- "Chernobyl S1E2" (English TV series) rated 3 overall and 4 in quality, with a missing creator.
- "Fermat's Last Theorem" (English non-fiction) rated 4 overall and 4 in quality.

Overall, the dataset presents a rich source of information regarding media ratings across different languages and types.

# Summary of the Dataset
This dataset contains 2,652 entries with 8 features, including media ratings, types, languages, and creators, and highlights the qualitative and quantitative aspects of media reviews.

# Histogram of features: ['overall', 'quality', 'repeatability']

Let us explore some of these features below



## Plot of feature: overall

![overall.plot.png](overall.plot.png)



## Plot of feature: quality

![quality.plot.png](quality.plot.png)



## Plot of feature: repeatability

![repeatability.plot.png](repeatability.plot.png)

