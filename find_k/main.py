import sys
import os
import time
sys.path.append(os.path.abspath('../lib'))

import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np

from file_functions import *
from normalize_functions import *
from K_Means import K_Means

DATASETS_PATH = '../assets/datasets/twitter/'
DATASET_NAME = 'collecte_libre_2'

DATA_FILENAME = DATASET_NAME + '.csv'
LABELS_FILENAME = DATASET_NAME + '_labels.csv'
CSV_SEPARATOR = ';'
RESULTS_PATH = "results"

K_VALUES = range(2, 10)

labels = read_csv_dataset(DATASETS_PATH + LABELS_FILENAME, CSV_SEPARATOR)
labels_names = labels[0]
dataset = read_csv_dataset(DATASETS_PATH + DATA_FILENAME, CSV_SEPARATOR, len(labels_names))

normalized_columns, normalizations_values, dataset = normalize(dataset)

for K in K_VALUES:

    print("===== K : " + str(K) + " =====")

    X = np.array(dataset, dtype=np.float_)

    clf = K_Means(K)
    clf.fit(X)

    plt.scatter(
        K,
        clf.get_average_distance(),
        color='b'
    )


plt.xlabel("k")
plt.ylabel("average distance feature/centroid")
plt.savefig(RESULTS_PATH + '/' + DATASET_NAME + '.svg')
