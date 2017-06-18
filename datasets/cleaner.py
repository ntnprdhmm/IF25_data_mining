import sys
import os
import time
sys.path.append(os.path.abspath('../lib'))

from file_functions import *

# files and columns to remove
FEATURES_FILE_NAME = 'twitter/manchester.csv'
LABELS_FILE_NAME = 'twitter/manchester_labels.csv'
CSV_SEPARATOR = ';'
TO_REMOVE = []

# load files
labels_names = read_csv_dataset(LABELS_FILE_NAME, CSV_SEPARATOR)[0]
features = read_csv_dataset(FEATURES_FILE_NAME, CSV_SEPARATOR, len(labels_names))

# get the colomn to remove
TO_REMOVE_INDEXES = []
for i in range(len(labels_names)):
    if labels_names[i] in TO_REMOVE:
        TO_REMOVE_INDEXES.append(i)

# clean labels
cleaned_labels_names = []
for i in range(len(labels_names)):
    if i not in TO_REMOVE_INDEXES:
        cleaned_labels_names.append(labels_names[i])
labels_names = cleaned_labels_names

# clean features
cleaned_features = []
for feature in features:
    cleaned_feature = []
    empty_columns = 0
    for i in range(len(feature)):
        if i not in TO_REMOVE_INDEXES:
            if len(str(feature[i])) > 0:
                cleaned_feature.append(str(feature[i]))
            else:
                empty_columns = empty_columns + 1
    if empty_columns == 0:
        cleaned_features.append(cleaned_feature)
features = cleaned_features

# override files with cleaned data
f = open(LABELS_FILE_NAME, 'w')

f.write(CSV_SEPARATOR.join(cleaned_labels_names))

f.close()

f = open(FEATURES_FILE_NAME, 'w')

for feature in features:
    f.write(CSV_SEPARATOR.join([str(v) for v in feature]) + '\n')

f.close()
