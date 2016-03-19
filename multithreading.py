#! /home/b51816/localpython/python3/bin/python3
import time , threading
lock = threading.Lock()
a = 10
def loop():
   global a
   for i in range(5):
      print("thread %s is running %s" % (threading.current_thread().name,i))
      time.sleep(1)
      lock.acquire()
      print("thread %s get lock" % threading.current_thread().name)
      try:
         a = a+i
      finally:
         print("a is %d" % a)
         lock.release()
   print("thread %s ended" % threading.current_thread().name)


print("thread %s start" % threading.current_thread().name)
child_t_1 = threading.Thread(target=loop,name="child_thread_1")
child_t_2 = threading.Thread(target=loop,name="child_thread_2")
child_t_1.start()
child_t_2.start()
child_t_1.join()
child_t_2.join()
loop()
child_t_3 = threading.Thread(target=loop,name="child_thread_3")
child_t_3.start()
child_t_3.join()
print("thread %s ended" % threading.current_thread().name)
import threading, multiprocessing
print("Current CPU Number is %d",% multiprocessing.cpu_count())
def loop():
    x = 0
    while True:
        x = x + 1
        print("thread %s , x is %d" % (threading.current_thread().name,x))

for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()
