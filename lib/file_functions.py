import os
import shutil

""" Read a csv dataset into a list
	Return this list
"""
def read_csv_dataset(f, separator = ',', length = None):
	data = []
	readfile = open(f, 'r')
	readlines = readfile.readlines()
	for line in readlines:
		line = line.rstrip() # remove the \n
		splited_line = line.split(separator)
		# check if attributes doesn't use the separator characters
		if not length or (length and len(splited_line) == length):
			row = []
			for v in splited_line:
				row.append(float(v) if isfloat(v) else v)
			data.append(row)
		else:
			print("[REJECTED] : " + line)
	return data

""" Remove all in a folder
"""
def empty_dir(dirpath):
	if os.path.isdir(dirpath):
		for f in os.listdir(dirpath):
			if os.path.isdir(dirpath + "/" + f):
				shutil.rmtree(dirpath + "/" + f)
			else:
				os.remove(dirpath + "/" + f)

""" Check if the value can be converted to float
"""
def isfloat(value):
	try:
		float(value)
		return True
	except ValueError:
		return False
