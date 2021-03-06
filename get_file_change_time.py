# !/usr/bin/python
#get_file_change_time.py


import os
import sys
import time
import re
import Tkinter

def is_leap_year (year) :
  if  ( year % 400 == 0 ) or ( year % 100 != 0 and year % 4 == 0) :
    return True
  else :
    return False 


def number_to_str_date (year, number) :
  month_date = [] #= [-1, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
  # leap_month_date = [-1, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366]
  month = "-"
  day = "-"
  if is_leap_year (year) and number <= 366:
    month_date = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366]
  elif number <= 365 :
    month_date = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
  else :
    print ("worng date number")
    return 
  for i in range (1, 13) :
    # print (i)
    if number <= month_date [i] :
      if i < 10 :
        month += "0" + str (i)
      else :
        month += str (i)
      nday =  number - month_date [i-1]
      if nday < 10 :
        day += "0" + str (nday)
      else:
        day += str (nday)
      # print month, day
      return str (year) + str (month) + str (day) 
      # break


def get_total_days_of_year (year) :
  if is_leap_year (int(year)) :
    return 366
  else :
    return 365


def get_year (str_date) :
  strs = re.split ("-", str_date)
  return int (strs[0])


def count_file_by_change_time (input_path, result_file) :
  dirs = os.listdir (input_path)
  count_date = {}
  for adir in dirs:
    afile =  os.path.join (input_path, adir)
    if os.path.isfile (afile) == True:
      t_date = time.strftime ('%Y-%m-%d', time.gmtime (os.path.getmtime (afile) + 8 * 3600))
      t_time = time.strftime ('%H:%M:%S', time.gmtime (os.path.getmtime (afile) + 8 * 3600))
      if t_date in count_date:
        count_date [t_date].append (t_time)
      else:
        count_date [t_date] = [t_time]
  
  for year in range (get_year (min (count_date)), get_year (max (count_date))+1) :
    for days in range (1, get_total_days_of_year (year) + 1) :
      str_day = number_to_str_date (year, days)
      if str_day not in count_date :
        count_date [str_day] = [] 
  # print year
  outfile = open (result_file, 'w')
  outfile.write ("date\tnumber of images\tstart time\tend time\tnumber of images took from 10:00-14:00\tstart_time\tend_time\r\n")
  for key in sorted (count_date):
    count_10_to_14 = 0
    time_list = count_date [key]
    if len (time_list) == 0 :
      outfile.write (str (key) + "\t" + str (len (time_list)) + "\t\t\t0\t\t\n")
      continue
    am_10_start = ""
    pm_14_end = ""
    for a_time in sorted (time_list) :
      if a_time >= "10:00:00" and a_time <= "14:00:00" :
        if count_10_to_14 == 0 :
          am_10_start = a_time
        if a_time > pm_14_end or pm_14_end == "MULL" :
          pm_14_end = a_time
        count_10_to_14 += 1
    print (str (key) + "\t" + str (len (time_list)) + "\t" + min (time_list) + "\t" + max (time_list) + "\t" + str (count_10_to_14) + 
      "\t" + str (am_10_start) + "\t" + str (pm_14_end) )
    outfile.write (str (key) + "\t" + str (len (time_list)) + "\t" + min (time_list) + "\t" + max (time_list) + "\t" + str (count_10_to_14) + 
      "\t" + str (am_10_start) + "\t" + str (pm_14_end) + "\n")
  outfile.close ()



    


if __name__ == "__main__":
  # top = Tkinter.Tk()
  # top.mainloop()
  root = Tkinter.Tk ()
  lb_title = Tkinter.Label (root,text='input path').pack ()
  text1 = Tkinter.Entry (root, width = 30)
  text1.pack ()
  lb_title = Tkinter.Label (root,text='output path').pack ()
  text2 = Tkinter.Entry (root, width = 30)
  text2.pack ()
  def start_click ():
    count_file_by_change_time (text1.get(), text2.get())
  def quit_click () :
    exit ()
  btn_start = Tkinter.Button(root, text = 'start', command = start_click ).pack (side = Tkinter.LEFT)
  btn_quit = Tkinter.Button(root, text = 'quit', command = root.destroy ).pack (side = Tkinter.RIGHT)
  root.mainloop()
  # config_file = open ("config.txt", "r")
  # input_path = config_file.readline ()
  # input_path = input_path.replace ("\n", "")
  # result_file = config_file.readline () 
  # result_file = result_file.replace ("\n", "")
  # config_file.close ()
  # count_file_by_change_time (input_path, result_file)
  
  
