import sys
import os
import time
sys.path.append(os.path.abspath('../lib'))

import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

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
K_VALUES = range(2, 7)
COLORS = ['b', 'g', 'r', 'c', 'm', 'y', 'k'] * 10

labels = read_csv_dataset(DATASETS_PATH + LABELS_FILENAME, CSV_SEPARATOR)
labels_names = labels[0]
labels_stats = labels[1]
dataset = read_csv_dataset(DATASETS_PATH + DATA_FILENAME, CSV_SEPARATOR, len(labels_names))

normalized_columns, normalizations_values, dataset = normalize(dataset)

# empty the /results folder
empty_dir(RESULTS_PATH)

for K in K_VALUES:

    print("\n==========" + len(str(K))*"=" + "======")
    print("===== K : " + str(K) + " =====")
    print("==========" + len(str(K))*"=" + "======\n")

    CLUSTER_RESULTS_PATH = RESULTS_PATH + "/k=" + str(K)
    os.makedirs(CLUSTER_RESULTS_PATH)

    X = np.array(dataset, dtype=np.float_)

    clf = K_Means(K)
    clf.fit(X)

    # for each attribut combination
    for i in range(len(labels_names)):
        for j in range(len(labels_names)):
            if i != j:

                start_time = time.time()

                print("\n" + labels_names[i] + " -- " + labels_names[j])

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
                plt.savefig(CLUSTER_RESULTS_PATH + '/' + labels_names[i] + '_' + labels_names[j] + '.svg')
                plt.clf()

                print("[DONE] %s in seconds \n" % str(time.time() - start_time))
