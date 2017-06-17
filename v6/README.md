# V4

## run the script

run the following command to show a result of K-Means:
```
python main.py
```

## script attributs

The datasets folder.
```
DATASETS_PATH = '../assets/datasets/'
```

The file which contains the features's labels.
```
LABELS_FILENAME = 'example_dataset_labels.csv'
```

The file which contains the features.
```
DATA_FILENAME = 'example_dataset.csv'
```

The separator used in your dataset.
```
CSV_SEPARATOR = ';'
```

All the values that K will to take
```
# specific values
K_VALUES = [1,2,5,6]

# a range (example: 1,2,3,4,5)
K_VALUES = range(1,6)
```

The output folder
```
RESULTS_PATH = "results"
```

The file base name for the unnormalized data of each cluster.
```
RESULTS_BASENAME = 'cluster_'
```

The file base name for the normalized data of each cluster.
```
CRUDE_RESULTS_BASENAME = "crude_cluster_"
```

The file base name for the stats of each cluster.
```
STATS_RESULTS_BASENAME = "stats_cluster_"
```
