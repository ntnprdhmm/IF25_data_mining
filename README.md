# IF25_data_mining

## v1

v1 is the first K_Means implementation we did, with a short dataset in 2 dimensions.

## v2

v2 can handle n-dimensions dataset and display basics results in the console.

## v3

v3 can handle n-dimensions data, normalize data and out detailled results for each cluster in files.

## v4

With v4, you can run k_means for a list of given values for K.

## file_functions.py

**/lib/file_functions.py**

### read_csv_dataset

import a csv file in a 2 dimensions list and remove the "unsplittable" feature. For example, if a feature's attribute uses the csv separator characters, this feature can't be splitted correctly.    

## cleaner.py

**/assets/datasets/cleaner.py**

This script can be use to clean a dataset, by removing columns.

```
FEATURES_FILE_NAME = 'example_dataset.csv'
LABELS_FILE_NAME = 'example_dataset_labels.csv'
CSV_SEPARATOR = ','
TO_REMOVE = ['colname1', 'colname2']
```
