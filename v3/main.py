import sys
import os
import time
sys.path.append(os.path.abspath('../lib'))

import numpy as np
import csv

from file_functions import *
from normalize_functions import *
from stats_functions import *
from K_Means import K_Means

DATASETS_PATH = '../assets/datasets/'
DATA_FILENAME = 'twitter/collecte_libre.csv'
LABELS_FILENAME = 'twitter/collecte_libre_labels.csv'
CSV_SEPARATOR = ';'

RESULTS_PATH = "results"
RESULTS_BASENAME = 'cluster_'
CRUDE_RESULTS_BASENAME = "crude_cluster_"
STATS_RESULTS_BASENAME = "stats_cluster_"
K = 5

labels = read_csv_dataset(DATASETS_PATH + LABELS_FILENAME, CSV_SEPARATOR)
labels_names = labels[0]
labels_stats = labels[1]
dataset = read_csv_dataset(DATASETS_PATH + DATA_FILENAME, CSV_SEPARATOR, len(labels_names))

normalized_columns, normalizations_values, dataset = normalize(dataset)

X = np.array(dataset)

clf = K_Means(K)
clf.fit(X)

# empty the /results folder
empty_dir(RESULTS_PATH)

for classification in clf.classifications:
    print("\n===== CLUSTER " + str(classification) + " =====")

    # write crude features of this cluster

    print("write crude data\n[START]")
    start_time = time.time()
    f = open(RESULTS_PATH + "/" + CRUDE_RESULTS_BASENAME + str(classification) + ".csv", 'a')

    for featureset in clf.classifications[classification]:
        f.write(",".join([str(v) for v in featureset]) + "\n")

    f.close()
    print("[DONE] %s in seconds \n" % str(time.time() - start_time))

    # write unnormalized features of this cluster

    print("write unnormalized data\n[START]")
    start_time = time.time()
    f = open(RESULTS_PATH + "/" + RESULTS_BASENAME + str(classification) + ".csv", 'a')

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
    print("[DONE] %s in seconds \n" % str(time.time() - start_time))

    # stats on this cluster

    print("write stats on this cluster\n[START]")
    start_time = time.time()
    f = open(RESULTS_PATH + "/" + STATS_RESULTS_BASENAME + str(classification) + ".txt", 'a')

    f.write('=' * (len(str(classification)) + 4 + 8) + "\n")
    f.write("= cluster " + str(classification) + " =\n")
    f.write('=' * (len(str(classification)) + 4 + 8) + "\n\n")

    f.write('Features in this cluster : ' + str(len(clf.classifications[classification])) + '\n\n')

    for i in range(len(labels_names)):

        f.write('-' * (len(labels_names[i]) + 4) + "\n")
        f.write("- " + labels_names[i].upper() + " -\n")
        f.write('-' * (len(labels_names[i]) + 4) + "\n\n")

        if labels_stats[i] == 1:
            if isfloat(unnormalized_dataset[0][i]):
                min, max, mean = get_col_mean_value(clf.classifications[classification], i)
                f.write("min %f\nmax %f\nmean %f" % (min, max, mean))
                f.write('\n\n')
            f.write(stringify_dic(get_col_values_percentages(unnormalized_dataset, i)))

        f.write('\n\n')

    f.close()
    print("[DONE] %s in seconds \n" % str(time.time() - start_time))

    print("=====================\n")
