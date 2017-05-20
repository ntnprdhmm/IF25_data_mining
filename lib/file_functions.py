""" Read a csv dataset into a list
	Return this list
"""
def read_csv_dataset(f):
    data = []
    readfile = open(f, 'r')
    readlines = readfile.readlines()
    for line in readlines:
        data.append([float(v) for v in line.split(',')])
    return data
