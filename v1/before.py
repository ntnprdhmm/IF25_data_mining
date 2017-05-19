#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
import csv
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

from lib.file import *

DATASETS_PATH = './assets/datasets/'
FILENAME = 'example1.csv'
COLOR = 'b'

dataset = read_csv_dataset(DATASETS_PATH + FILENAME)

for point in dataset:
    plt.scatter(
        point[0],
        point[1],
        marker='x',
        color=COLOR,
        s=150,
        linewidths=5,
    )

plt.show()


			
