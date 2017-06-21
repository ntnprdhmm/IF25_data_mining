import sys
import os
import time
sys.path.append(os.path.abspath('./lib'))

import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

import numpy as np
import csv

from file_functions import *
from normalize_functions import *
from stats_functions import *
from K_Means import K_Means

DATASETS_PATH = './datasets/twitter/'
DATASET_NAME = 'libre'
CSV_SEPARATOR = ';'
K_VALUES = [3]

DATA_FILENAME = DATASET_NAME + '.csv'
LABELS_FILENAME = DATASET_NAME + '_labels.csv'
RESULTS_PATH = "./results/kmeans"
COLORS = ["#673AB7", "#E91E63", "#3F51B5", "#2196F3", "#00BCD4", "#009688", "#4CAF50", "#CDDC39", "#FFEB3B", "#FF9800", "#795548"]

labels = read_csv_dataset(DATASETS_PATH + LABELS_FILENAME, CSV_SEPARATOR)
labels_names = labels[0]
dataset = read_csv_dataset(DATASETS_PATH + DATA_FILENAME, CSV_SEPARATOR, len(labels_names))

normalized_columns, normalizations_values, dataset = normalize(dataset)

# empty the /results folder
empty_dir(RESULTS_PATH)

nb_combinations = 0
# create a folder for each attribut combination
for i in range(len(labels_names)):
    for j in range(i+1, len(labels_names)):

        os.makedirs(RESULTS_PATH + '/' + labels_names[i] + '_' + labels_names[j])
        nb_combinations = nb_combinations + 1

for K in K_VALUES:

    start_time = time.time()

    print("\n==========" + len(str(K))*"=" + "======")
    print("===== K : " + str(K) + " =====")
    print("==========" + len(str(K))*"=" + "======\n")

    X = np.array(dataset, dtype=np.float_)

    clf = K_Means(K)
    clf.fit(X)

    combinations_done = 0
    # for each attribut combination
    for i in range(len(labels_names)):
        for j in range(i + 1, len(labels_names)):

                # loop through clusters
                for classification in clf.classifications:

                    # loop through the features of this cluster
                    for feature in clf.classifications[classification]:
                        # plot this feature with the 2 current attributes
                        plt.scatter(
                            feature[i],
                            feature[j],
                            color=COLORS[classification]
                        )

                # save the plotted graph
                plt.xlabel(labels_names[i])
                plt.ylabel(labels_names[j])
                plt.savefig(RESULTS_PATH + '/' + labels_names[i] + '_' + labels_names[j] + '/k=' + str(classification + 1) + '.svg')
                plt.clf()

                combinations_done = combinations_done + 1
                print("DONE : " + str(combinations_done/nb_combinations))

    print("[CLUSTER DONE] %s in seconds \n" % str(time.time() - start_time))
