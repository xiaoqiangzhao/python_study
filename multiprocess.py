#! /home/b51816/localpython/python3/bin/python3

import os
print('Current Process Id is : %s' % os.getpid())

pid = os.fork()
if pid == 0:
   print("This is Child Process with ID %s" % os.getpid())
else:
   print("This is Parent Process with ID %s, I have a child Process with ID : %s" % (os.getpid(), pid))

from multiprocessing import Process
import time
def run_child(n):
   for i in range(n):
      print("Count %d" % (n-i))
      time.sleep(1)
if pid == 0:
   print('Parent Process ID : %s' % os.getpid())
   child_p = Process(target=run_child,args=(10,))
   child_p_2 = Process(target=run_child,args=(20,))
   child_p.start()
   child_p_2.start()
   print('wait for child process')
   child_p.join()
   print('child 1 process end')
   child_p_2.join()
   print('child 2 process end')
