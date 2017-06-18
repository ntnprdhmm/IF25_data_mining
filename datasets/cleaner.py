import sys
import os
import time
sys.path.append(os.path.abspath('../lib'))

from file_functions import *

# files and columns to remove
FEATURES_FILE_NAME = 'twitter/collecte_libre_2.csv'
LABELS_FILE_NAME = 'twitter/collecte_libre_2_labels.csv'
CSV_SEPARATOR = ';'
TO_REMOVE = ['sum(t.nbhashtags)']

# load files
labels = read_csv_dataset(LABELS_FILE_NAME, CSV_SEPARATOR)
labels_names = labels[0]
labels_stats = labels[1]
features = read_csv_dataset(FEATURES_FILE_NAME, CSV_SEPARATOR, len(labels_names))

# get the colomn to remove
TO_REMOVE_INDEXES = []
for i in range(len(labels_names)):
    if labels_names[i] in TO_REMOVE:
        TO_REMOVE_INDEXES.append(i)

# continue only if there are columns to remove
if len(TO_REMOVE_INDEXES) > 0:

    # clean labels
    cleaned_labels_names = []
    cleaned_labels_stats = []
    for i in range(len(labels_names)):
        if i not in TO_REMOVE_INDEXES:
            cleaned_labels_names.append(labels_names[i])
            cleaned_labels_stats.append(str(int(labels_stats[i])))
    labels_names = cleaned_labels_names
    labels_stats = cleaned_labels_stats

    # clean features
    cleaned_features = []
    for feature in features:
        cleaned_feature = []
        for i in range(len(feature)):
            if i not in TO_REMOVE_INDEXES:
                cleaned_feature.append(str(feature[i]))
        cleaned_features.append(cleaned_feature)
    features = cleaned_features

    # override files with cleaned data
    f = open(LABELS_FILE_NAME, 'w')

    f.write(CSV_SEPARATOR.join(cleaned_labels_names))
    f.write('\n')
    f.write(CSV_SEPARATOR.join(cleaned_labels_stats))

    f.close()

    f = open(FEATURES_FILE_NAME, 'w')

    for feature in features:
        f.write(CSV_SEPARATOR.join([str(v) for v in feature]) + '\n')

    f.close()
