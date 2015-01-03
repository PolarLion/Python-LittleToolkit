# !/usr/bin/python
#get_file_change_time.py


import os
import sys
import time
import re

if __name__ == "__main__":
  #use your own path
  path = "D:\\documents\\C++\\C++language\\"
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
  filename1 = "C:\\Users\\xuewen\\Desktop\\res1.txt"
  outfile = open (filename1, 'w')
  outfile.write ("date\tnumber of images\tstart time\tend time\tnumber of images took from 10:00-14:00\tstart_time\tend_time\r\n")
  for key in sorted (count_change_time):
    count_10_to_14 = 0
    time_list = count_change_time [key]
    am_10_start = ""
    pm_14_end = ""
    for time in sorted (time_list) :
      if time >= "10:00:00" and time <= "14:00:00" :
        if count_10_to_14 == 0 :
          am_10_start = time
        if time > pm_14_end or pm_14_end == "MULL" :
          pm_14_end = time
        count_10_to_14 += 1
    print (str (key) + "\t" + str (len (time_list)) + "\t" + min (time_list) + "\t" + max (time_list) + "\t" + str (count_10_to_14) + 
      "\t" + str (am_10_start) + "\t" + str (pm_14_end) + "\r\n")
    outfile.write (str (key) + "\t" + str (len (time_list)) + "\t" + min (time_list) + "\t" + max (time_list) + "\t" + str (count_10_to_14) + 
      "\t" + str (am_10_start) + "\t" + str (pm_14_end) + "\r\n")
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
