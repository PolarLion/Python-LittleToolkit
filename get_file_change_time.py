# !/usr/bin/python
#get_file_change_time.py


import os
import sys
import time
import re

if __name__ == "__main__":
  #use your own path
  path = "D:\\documents\\C++\\lion's c++\\程序00\\c++\\"
  dirs = os.listdir (path)
  count_change_time = {}
  for adir in dirs:
    afile =  os.path.join (path, adir)
    if os.path.isfile (afile) == True:
      t_date = time.strftime ('%Y-%m-%d', time.gmtime (os.path.getmtime (afile)))
      t_time = time.strftime ('%H:%M:%S', time.gmtime (os.path.getmtime (afile)))
      if t_date in count_change_time:
        count_change_time [t_date].append (t_time)
      else:
        count_change_time [t_date] = [t_time]
  #use your own path
  filename = "C:\\Users\\xuewen\\Desktop\\res.txt"
  outfile = open (filename, 'w')
  outfile.write ("date\tnumber of images\tstart time\tend time\r\n")
  for key in sorted (count_change_time):
    count_hour = {}
    time_list = count_change_time [key]
    print (str (key) + "\t" + str (len (time_list)) + "\t" + min (time_list) + "\t" + max (time_list))
    outfile.write (str (key) + "\t" + str (len (time_list)) + "\t" + min (time_list) + "\t" + max (time_list) + "\r\n")
##    for t_time in time_list:
##      t_hour = t_time [0:2]
##      if t_hour in count_hour :
##        count_hour [t_hour] += 1
##      else:
##        count_hour [t_hour] = 1
##    
##    print str(key) + "\t" + str (len(alist)) + "\t" + str (alist)
##    outfile.write (str(key) + "\t" + str (len(alist)) + "\t" + str (alist) + "\r\n")
  outfile.close ()
