#This script is to concatenate all txt files created when test.py script is runed

import glob

paths = glob.glob("result/*.txt")
final = ''

for name in paths:
	doc = open(name)
	final +=doc.read()
doc.close()
d = open('result/final.dat', 'w')
d.write(final)
d.close()
