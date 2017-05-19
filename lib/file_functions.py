""" Read a csv dataset into a list
	Return this list
"""
def read_csv_dataset(f):
    data = []
    readfile = open(f, 'r')
    readlines = readfile.readlines()
    for line in readlines:
        pt = line.split(',')
        y = float(pt[0])
        z = float(pt[1])
        data.append([y, z])
    return data
