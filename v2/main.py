import sys
import os
sys.path.append(os.path.abspath('../lib'))

import numpy as np
import csv

from file_functions import *
from K_Means import K_Means

DATASETS_PATH = '../assets/datasets/'
FILENAME = 'example2.csv'
RESULTS_PATH = "results"
RESULTS_BASENAME = "cluster_"
K = 6

dataset = read_csv_dataset(DATASETS_PATH + FILENAME)
X = np.array(dataset)

clf = K_Means(K)
clf.fit(X)

# empty the /results folder
empty_dir(RESULTS_PATH)

for classification in clf.classifications:
    print("\n===== CLUSTER " + str(classification) + " =====")

    feature_percentage = len(clf.classifications[classification]) / len(dataset) * 100
    print(feature_percentage)

    f = open(RESULTS_PATH + "/" + RESULTS_BASENAME + str(classification) + ".out", 'a')

    f.write("CLUSTER COORDINATES : " + ",".join([str(v) for v in clf.centroids[classification]]) + "\n")
    f.write("PERCENTAGE : " + str(feature_percentage) + "\n\n")

    for featureset in clf.classifications[classification]:
        f.write(",".join([str(v) for v in featureset]) + "\n")

    f.close()

    print("=====================\n")
