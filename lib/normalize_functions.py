import os

""" call normalize_column for each column to normalize
"""
def normalize_columns(columns, dataset):
    for column in columns:
        dataset = normalize_column(dataset, column)
    return dataset

""" normalize the given column in the dataset
"""
def normalize_column(dataset, col_number):
    dic = {}
    counter = 1
    for i in range(len(dataset)):
        if dataset[i][col_number] not in dic:
            dic[dataset[i][col_number]] = counter
            counter += 1
        dataset[i][col_number] = dic[dataset[i][col_number]]
    return dataset

""" normalize the dataset
"""
def normalize(dataset):
    a = []
    for v in range(len(dataset[0])):
        if isinstance(dataset[0][v], str):
            a.append(v)
    return normalize_columns(a, dataset)
