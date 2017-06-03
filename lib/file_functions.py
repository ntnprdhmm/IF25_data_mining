import os

""" Read a csv dataset into a list
	Return this list
"""
def read_csv_dataset(f):
	data = []
	readfile = open(f, 'r')
	readlines = readfile.readlines()
	for line in readlines:
		line = line.rstrip() # remove the \n
		row = []
		for v in line.split(','):
			row.append(float(v) if isfloat(v) else v)
		data.append(row)
	return data

""" Remove all files in the given directory
"""
def empty_dir(dirpath):
	if os.path.isdir(dirpath):
		for f in os.listdir(dirpath):
			os.remove(dirpath + "/" + f)

""" Check if the value can be converted to float
"""
def isfloat(value):
	try:
		float(value)
		return True
	except ValueError:
		return False
