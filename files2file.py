#!/usr/bin/python
#files2file.py


import os
import sys
import re

def gb2312_to_utf_8 (gbk_str):
    unicode_str = gbk_str.decode ('gb2312', errors = 'ignore')
    return unicode_str.encode ('utf-8')
    


def files2file (path, filename) :
    pattern = re.compile (r'<content>.*</content>')
    outfile = open (filename, 'w')
    files = os.listdir (path)
    i = 0;
    for a_file in files :
        a_file = os.path.join (path, a_file)
        infile = open (a_file, 'r')
        i += 1;
        #utf8_file = gb2312_to_utf_8 (infile.read ())
        #for content in pattern.finditer (utf8_file) :
        for content in pattern.finditer (infile.read ()) :
            outfile.write (content.group () + "\n")
        infile.close ()
        #if i > 1 :
         #   break
    print (i)
    outfile.close ()



if __name__ == "__main__" :
    path = "../data"
    filename = "gbk_test.txt"
    files2file (path, filename)



