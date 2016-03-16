#! /home/b51816/localpython/python3/bin/python3
import sys
import os
find_type = sys.argv[2]
current_dir = sys.argv[1]
key_word = sys.argv[3]
print("Current Directory : %s\nFind Type : %s\nKey Word: %s\n" % (os.path.abspath(current_dir),find_type,key_word))
def my_search(d,t,w):   ## type dir word
   tp = 'dir'
   c_d =os.path.abspath(d)
   # print(c_d)
   dirs = [x for x in os.listdir(d) if os.path.isdir(os.path.join(c_d,x))]  ## need abs path for each dir and file found
   files = [x for x in os.listdir(d) if os.path.isfile(os.path.join(c_d,x))]
   # print("found: ",d,c_d,files)
   for m_d in dirs:
      my_search(os.path.join(d,m_d),t,w)
   if tp in t:
      # print('looking for dir',t)
      for m_d in dirs:
         if w in m_d:
            print(os.path.join(c_d,m_d))
   else:
      # print('looking for file in ',c_d,files)
      for m_f in files:
         if w in m_f:
            print(os.path.join(c_d,m_f))
my_search(current_dir,find_type,key_word)

