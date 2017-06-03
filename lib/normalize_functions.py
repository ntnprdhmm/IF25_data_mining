import os

""" call normalize_column for each column to normalize
"""
def normalize_columns(columns, dataset):
    normalizations = {}
    for column in columns:
        column_normalizations, dataset = normalize_column(dataset, column)
        normalizations[column] = column_normalizations
    return normalizations, dataset

""" normalize the given column in the dataset
"""
def normalize_column(dataset, col_number):
    dic = {}
    inversed_dic = {}
    counter = 1
    for i in range(len(dataset)):
        if dataset[i][col_number] not in dic:
            dic[dataset[i][col_number]] = counter
            inversed_dic[counter] = dataset[i][col_number]
            counter += 1
        dataset[i][col_number] = dic[dataset[i][col_number]]
    return inversed_dic, dataset

""" normalize the dataset
"""
def normalize(dataset):
    a = []
    for v in range(len(dataset[0])):
        if isinstance(dataset[0][v], str):
            a.append(v)
    normalizations_values, dataset = normalize_columns(a, dataset)
    return a, normalizations_values ,dataset
