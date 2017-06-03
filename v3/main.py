import sys
import os
sys.path.append(os.path.abspath('../lib'))

import numpy as np
import csv

from file_functions import *
from normalize_functions import *
from stats_functions import *
from K_Means import K_Means

DATASETS_PATH = '../assets/datasets/'
DATA_FILENAME = 'example3.csv'
LABELS_FILENAME = 'example3_labels.csv'

RESULTS_PATH = "results"
RESULTS_BASENAME = 'cluster_'
CRUDE_RESULTS_BASENAME = "crude_cluster_"
K = 4

labels = read_csv_dataset(DATASETS_PATH + LABELS_FILENAME)[0]
dataset = read_csv_dataset(DATASETS_PATH + DATA_FILENAME)

normalized_columns, normalizations_values, dataset = normalize(dataset)
print(labels)

X = np.array(dataset)

clf = K_Means(K)
clf.fit(X)

# empty the /results folder
empty_dir(RESULTS_PATH)

for classification in clf.classifications:
    print("\n===== CLUSTER " + str(classification) + " =====")

    # write crud features of this cluster

    f = open(RESULTS_PATH + "/" + CRUDE_RESULTS_BASENAME + str(classification) + ".out", 'a')

    for featureset in clf.classifications[classification]:
        f.write(",".join([str(v) for v in featureset]) + "\n")

    f.close()

    # write unnormalized features of this cluster

    f = open(RESULTS_PATH + "/" + RESULTS_BASENAME + str(classification) + ".out", 'a')

    unnormalized_dataset = []
    for featureset in clf.classifications[classification]:
        values = []

        for i in range(len(featureset)):
            if i in normalizations_values:
                values.append(normalizations_values[i][featureset[i]])
            else:
                values.append(str(featureset[i]))

        unnormalized_dataset.append(values)
        f.write(",".join(values) + "\n")

    f.close()

    # stats on this cluster

    print(get_col_values_percentages(unnormalized_dataset, 0))

    min, max, mean = get_col_mean_value(clf.classifications[classification], 1)
    print(labels[1] + " on %d profiles: min %f - max %f - mean %f" % (len(clf.classifications[classification]), min, max, mean))

    print(get_col_values_percentages(unnormalized_dataset, 2))

    print("=====================\n")
