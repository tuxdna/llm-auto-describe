# Dataset Description

## Overview
The dataset consists of 10,000 entries and 23 features related to books, capturing various attributes such as identification numbers, author information, publication details, ratings, and images. 

## Shape of Data
- **Total Rows:** 10,000
- **Total Columns:** 23

## Data Types of Features
The dataset contains a mix of integer, float, and object (string) data types:
- **Integer Features:**
  - `book_id`: int64
  - `goodreads_book_id`: int64
  - `best_book_id`: int64
  - `work_id`: int64
  - `books_count`: int64
  - `ratings_count`: int64
  - `work_ratings_count`: int64
  - `work_text_reviews_count`: int64
  - `ratings_1`: int64
  - `ratings_2`: int64
  - `ratings_3`: int64
  - `ratings_4`: int64
  - `ratings_5`: int64

- **Float Features:**
  - `isbn13`: float64
  - `original_publication_year`: float64
  - `average_rating`: float64

- **Object Features:**
  - `isbn`: object
  - `authors`: object
  - `original_title`: object
  - `title`: object
  - `language_code`: object
  - `image_url`: object
  - `small_image_url`: object

## Null Counts of Features
Certain features contain null values:
- `isbn`: 700 missing values
- `isbn13`: 585 missing values
- `original_publication_year`: 21 missing values
- `original_title`: 585 missing values
- `language_code`: 1084 missing values

All other features have no missing values.

## Descriptive Statistics of Numeric Features
The following statistics are provided for numeric features:

| Feature                        | Count       | Mean          | Std Dev      | Min     | 25%     | 50%     | 75%     | Max        |
|--------------------------------|-------------|---------------|--------------|---------|---------|---------|---------|------------|
| `book_id`                     | 10,000     | 5000.50       | 2886.90      | 1       | 2500.75 | 5000.50 | 7500.25 | 10,000     |
| `goodreads_book_id`           | 10,000     | 5,264,697     | 7,575,462    | 1       | 46,275  | 394,965 | 9,382,225 | 33,288,640 |
| `best_book_id`                | 10,000     | 5,471,214     | 7,827,330    | 1       | 47,911  | 425,123 | 9,636,112 | 35,534,230 |
| `work_id`                     | 10,000     | 8,646,183     | 11,751,060   | 87      | 1,008,841 | 2,719,524 | 14,517,750 | 56,399,600 |
| `books_count`                 | 10,000     | 75.71         | 170.47       | 1       | 23      | 40      | 67      | 3,455      |
| `isbn13`                      | 9,415      | 9.78049e+12   | N/A          | N/A     | N/A     | N/A     | N/A     | N/A        |
| `original_publication_year`   | 9,979      | (value)       | (value)      | (value) | (value) | (value) | (value) | (value)    |
| `average_rating`              | 10,000     | 4.02          | 0.43         | 3.12    | 3.77    | 4.02    | 4.44    | 5.00       |
| `ratings_count`               | 10,000     | 17,023        | 11,723       | 11      | 1,830   | 12,204  | 20,489  | 456,191    |
| `work_ratings_count`          | 10,000     | 19,227        | 13,114       | 30      | 2,056   | 13,196  | 23,502  | 436,802    |
| `work_text_reviews_count`     | 10,000     | 2,532         | 3,569        | 0       | 185     | 638     | 2,394   | 79,331     |
| `ratings_1`                   | 10,000     | 1,345         | 6,635        | 11      | 196     | 391     | 885     | 456,191    |
| `ratings_2`                   | 10,000     | 3,110         | 9,717        | 30      | 656     | 1,163   | 2,353   | 436,802    |
| `ratings_3`                   | 10,000     | 11,475        | 28,546       | 323     | 3,112   | 4,894   | 9,287   | 793,319    |
| `ratings_4`                   | 10,000     | 19,966        | 51,447       | 750     | 5,405   | 8,269   | 16,023  | 1,481,305  |
| `ratings_5`                   | 10,000     | 23,789        | 79,768       | 752     | 5,334   | 8,836   | 17,304  | 3,011,543  |

## Sample Data
Here are ten sample entries from the dataset:

|      | book_id | goodreads_book_id | best_book_id | work_id | books_count | isbn        | isbn13      | authors                                     | original_publication_year | original_title                                                            | title                                                                     | language_code | average_rating | ratings_count | work_ratings_count | work_text_reviews_count | ratings_1 | ratings_2 | ratings_3 | ratings_4 | ratings_5 | image_url                                                                                | small_image_url                                                                        |
|-----:|---------:|------------------:|--------------:|--------:|------------:|-------------:|-------------:|:--------------------------------------------|---------------------------:|:--------------------------------------------------------------------------|:--------------------------------------------------------------------------|:--------------|----------------:|----------------:|---------------------:|--------------------------:|------------:|-----------:|-----------:|-----------:|-----------:|:-----------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------|
| 6750 |     6751 |             285500 |         285500 |  1694397 |           57 |  553214829  | 9.78055e+12 | Founding Fathers                            |                        1776 | The Declaration of Independence and The Constitution of the United States | The Declaration of Independence and The Constitution of the United States | nan           |             4.44 |           14047 |                17123 |                       256 |         208 |         533 |        1846 |        3392 |       11144 | https://images.gr-assets.com/books/1320508156m/285500.jpg                                | https://images.gr-assets.com/books/1320508156s/285500.jpg                              |
| 5049 |     5050 |            9545064 |        9545064 | 13472700 |           34 |  446574465  | 9.78045e+12 | Rachel Simon                                |                        2011 | The Story of Beautiful Girl                                               | The Story of Beautiful Girl                                               | nan           |             3.92 |           19655 |                22401 |                      3517 |         279 |        1111 |        5172 |        9503 |        6336 | https://images.gr-assets.com/books/1336851169m/9545064.jpg                               | https://images.gr-assets.com/books/1336851169s/9545064.jpg                             |
| 4574 |     4575 |             867248 |         867248 |   650820 |           21 |  689831870  | 9.78069e+12 | Karma Wilson, Jane Chapman                  |                        2002 | Bear Snores On                                                            | Bear Snores On                                                            | en-US         |             4.25 |           24556 |                24814 |                       604 |         275 |         735 |        4007 |        7408 |       12389 | https://images.gr-assets.com/books/1344390790m/867248.jpg                                | https://images.gr-assets.com/books/1344390790s/867248.jpg                              |
| 5930 |     5931 |               20563 |          20563 | 21503633 |          390 |  375759018  | 9.78038e+12 | George Eliot, Joanna Trollope, Hugh Osborne |                        1859 | Adam Bede                                                                 | Adam Bede                                                                 | nan           |             3.77 |           17777 |                19423 |                       659 |         650 |        1475 |        4959 |        6999 |        5340 | https://s.gr-assets.com/assets/nophoto/book/111x148-bcc042a9c91a29c1d680899eff700a03.png | https://s.gr-assets.com/assets/nophoto/book/50x75-a91bf249278a81aabab721ef782c4a74.png |
| 3649 |     3650 |                6748 |           6748 |       574 |           46 |  316925284  | 9.78032e+12 | David Foster Wallace                        |                        1996 | A Supposedly Fun Thing I'll Never Do Again: Essays and Arguments          | A Supposedly Fun Thing I'll Never Do Again:  Essays and Arguments         | en-GB         |             4.28 |           23272 |                26763 |                      2098 |         266 |         656 |        3045 |       10238 |       12558 | https://s.gr-assets.com/assets/nophoto/book/111x148-bcc042a9c91a29c1d680899eff700a03.png | https://s.gr-assets.com/assets/nophoto/book/50x75-a91bf249278a81aabab721ef782c4a74.png |
| 2146 |     2147 |            2586771 |        2586771 |  2604190 |           39 | 1400063973  | 9.7814e+12  | David Ebershoff                             |                        2008 | The 19th Wife                                                             | The 19th Wife                                                             | en-US         |             3.63 |           44921 |                50034 |                      6018 |        1014 |        3888 |       16023 |       20874 |        8235 | https://s.gr-assets.com/assets/nophoto/book/111x148-bcc042a9c91a29c1d680899eff700a03.png | https://s.gr-assets.com/assets/nophoto/book/50x75-a91bf249278a81aabab721ef782c4a74.png |
| 9147 |     9148 |             111306 |         111306 |   107202 |           28 |  821780654  | 9.78082e+12 | Jacquelyn Frank                             |                        2006 | Jacob                                                                     | Jacob (Nightwalkers, #1)                                                  | eng           |             4.02 |           17448 |                18356 |                       872 |         490 |         983 |        3422 |        6187 |        7274 | https://s.gr-assets.com/assets/nophoto/book/111x148-bcc042a9c91a29c1d680899eff700a03.png | https://s.gr-assets.com/assets/nophoto/book/50x75-a91bf249278a81aabab721ef782c4a74.png |
| 5004 |     5005 |               46674 |          46674 |  1892311 |           42 |  380810336  | 9.78038e+12 | David D. Burns                              |                        1980 | Feeling Good: The New Mood Therapy                                        | Feeling Good: The New Mood Therapy                                        | en-US         |             3.95 |           17065 |                18208 |                       540 |         584 |        1127 |        3881 |        5692 |        6924 | https://s.gr-assets.com/assets/nophoto/book/111x148-bcc042a9c91a29c1d680899eff700a03.png | https://s.gr-assets.com/assets/nophoto/book/50x75-a91bf249278a81aabab721ef782c4a74.png |
| 6349 |     6350 |             555500 |         555500 |  2690582 |           26 |  786837888  | 9.78079e+12 | Dave Barry, Ridley Pearson, Greg Call       |                        2007 | Peter and the Secret of Rundoon                                           | Peter and the Secret of Rundoon (Peter and the Starcatchers, #3)          | en-US         |             4.16 |           18570 |                19299 |                       858 |         246 |         522 |        3476 |        6702 |        8353 | https://s.gr-assets.com/assets/nophoto/book/111x148-bcc042a9c91a29c1d680899eff700a03.png | https://s.gr-assets.com/assets/nophoto/book/50x75-a91bf249278a81aabab721ef782c4a74.png |
| 3876 |     3877 |            10047589 |       10047589 | 14943502 |           22 |  307596850  | 9.78031e+12 | Jennifer Close                              |                        2011 | Girls in White Dresses                                                    | Girls in White Dresses                                                    | eng           |             3.12 |           25167 |                27866 |                      2984 |        2392 |        5526 |        9757 |        6717 |        3474 | https://images.gr-assets.com/books/1320442277m/10047589.jpg                              | https://images.gr-assets.com/books/1320442277s/10047589.jpg                            |

# Histogram of features: ['isbn13', 'original_publication_year', 'average_rating', 'ratings_count', 'work_ratings_count', 'work_text_reviews_count', 'ratings_1', 'ratings_2', 'ratings_3', 'ratings_4', 'ratings_5']

Let us explore some features below



## Plot of feature: average_rating

![average_rating.plot.png](average_rating.plot.png)


## Plot of feature: ratings_count

![ratings_count.plot.png](ratings_count.plot.png)


## Plot of feature: work_ratings_count

![work_ratings_count.plot.png](work_ratings_count.plot.png)
