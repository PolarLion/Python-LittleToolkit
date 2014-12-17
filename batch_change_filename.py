# !/usr/bin/python
#change_filenmae.py


import os
import sys


if __name__ == "__main__":
	path = sys.argv[1]
	# path = "/home/lion/tc/training_set/easy_train/"
	dirs = os.listdir (path)
	for adir in dirs :
		newpath = os.path.join (path, adir)
		if os.path.isdir (newpath) == True :
			files = os.listdir (newpath)
			for afile in files :
				newname = adir+"_"+afile
				os.rename (os.path.join (newpath, afile), os.path.join (newpath, newname))