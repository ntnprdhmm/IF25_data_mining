import os

""" Return the mean value of the column of the given dataset
"""
def get_col_mean_value(dataset, col):
    min = 1000000000000
    max = 0
    mean = 0

    for feature in dataset:
        if feature[col] > max:
            max = feature[col]
        if feature[col] < min:
            min = feature[col]
        mean = mean + feature[col]

    mean = mean / len(dataset)

    return min, max, mean

""" Return the percentage of each value of a column
"""
def get_col_values_percentages(dataset, col):
    dic = {}

    for feature in dataset:
        if feature[col] in dic:
            dic[feature[col]] = dic[feature[col]] + 1
        else:
            dic[feature[col]] = 1

    for value in dic:
        dic[value] = dic[value] / len(dataset)

    return dic
