#! /home/b51816/localpython/python3/bin/python3
import sys
import os
key_word = sys.argv[0]
def found_file(d,w):
   c_d =os.path.abspath(d)
   # print(c_d)
   dirs = [x for x in os.listdir(d) if os.path.isdir(x)]
   files = [x for x in os.listdir(d) if os.path.isfile(x)]
   for m_d in dirs:
      found_file(os.path.join(d,m_d),w)
   for m_f in files:
      if w in m_f:
         print(os.path.join(c_d,m_f))
found_file('.','bal')   ## example usage
