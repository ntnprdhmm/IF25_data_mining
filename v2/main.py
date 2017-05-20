import sys
import os
sys.path.append(os.path.abspath('../lib'))

import numpy as np
import csv

from file_functions import *
from K_Means import K_Means

DATASETS_PATH = '../assets/datasets/'
FILENAME = 'example2.csv'
K = 2

dataset = read_csv_dataset(DATASETS_PATH + FILENAME)
X = np.array(dataset)

clf = K_Means(K)
clf.fit(X)

print(clf.centroids)

for classification in clf.classifications:
    print("===== CLUSTER " + str(classification) + " =====")
    print(str(len(clf.classifications[classification]) / len(dataset) * 100))
    print("=====================")
