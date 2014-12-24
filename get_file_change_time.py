# !/usr/bin/python
#get_file_change_time.py


import os
import sys
# import datetime
import time

if __name__ == "__main__":
	path = sys.argv[1]
	# path = ""
	dirs = os.listdir (path)
	count_change_time = {}
	for adir in dirs:
		afile =  os.path.join (path, adir)
		if os.path.isfile (afile) == True:
			dtime = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(os.path.getmtime (afile)))
			# dtime = str (datetime.timedelta(os.path.getmtime (afile)))
			if dtime in count_change_time:
				count_change_time [dtime] += 1
			else:
				count_change_time [dtime] = 1

	# filename = ".txt"
	outfile = open (sys.argv[2], 'w')
	# outfile = open (filename, 'w')
	# print ("hello world")
	# print len (count_change_time)
	for key in sorted(count_change_time):
		print str(key) + "\t" + str(count_change_time[key])
		outfile.write (str(key) + "\t" + str(count_change_time[key]) + "\r\n")
	outfile.close ()
