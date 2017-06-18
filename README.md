# IF25_data_mining

K_MEANS implementation.

## datasets

**/datasets**

### cleaner.py

***cleaner*** is a script to clean a given ***.csv*** file. It will remove all the unusable features and remove the given columns.

The ***.csv*** file which contains the features.
```
FEATURES_FILE_NAME = 'my_dataset.csv'
```

The ***.csv*** file which contains the columns's labels.
```
LABELS_FILE_NAME = 'my_dataset_labels.csv'
```

The separator used in the dataset.
```
CSV_SEPARATOR = ';'
```

The columns to remove
```
TO_REMOVE = ['sum(t.nbhashtags)']
```

### .csv files

A dataset is 2 ***.csv*** files :
- the first file contains the features. His name must be **[dataset_name].csv**
- the second file contains the labels. His name must be **[dataset_name]_labels.csv**

## main.py

**/main.py**

### script details

This script will run the kmeans algorithm for many values of K on a given dataset.

The folder that contains the dataset's files.
```
DATASETS_PATH = './datasets/twitter/'
```

The name of the dataset.
```
DATASET_NAME = 'collecte_libre_2'
```

The separator used in the dataset.
```
CSV_SEPARATOR = ';'
```

The values of K. **It has to be an array**, even if you want to run the algorithm for only one value of K.
```
K_VALUES = [2,6]
```

### output

You can find the ouput of the algorithm in **/results/kmeans**.

## find_k.py

**/find_k.py**

### script details

This script is used to calculate the curve of the mean distance centroid/feature for each cluster according to the value of K for a given dataset.

### output

You can find the ouput of the script in **/results/find_k**.

## lib

**/lib**

This folder contains functions and classes, used in the scripts, like the **K_Means** class to run the kmeans algorithm, or functions to read ***.csv*** files.
