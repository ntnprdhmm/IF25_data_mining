import sys
import os
sys.path.append(os.path.abspath('../lib'))

import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np
import csv

from file_functions import *
from K_Means import K_Means

DATASETS_PATH = '../assets/datasets/'
FILENAME = 'example1.csv'
COLORS = 10 * ['g', 'r', 'c', 'b', 'k']
K = 3

dataset = read_csv_dataset(DATASETS_PATH + FILENAME)
X = np.array(dataset)

clf = K_Means(K)
clf.fit(X)

for centroid in clf.centroids:
    plt.scatter(
        clf.centroids[centroid][0],
        clf.centroids[centroid][1],
        marker='o',
        color='k',
        s=150,
        linewidths=5,
        )

for classification in clf.classifications:
    color = COLORS[classification]
    for featureset in clf.classifications[classification]:
        plt.scatter(
            featureset[0],
            featureset[1],
            marker='x',
            color=color,
            s=150,
            linewidths=5,
            )

plt.show()
