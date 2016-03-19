#! /home/b51816/localpython/python3/bin/python3
import time,sys,queue
from multiprocessing.managers import BaseManager
class QueueManager(BaseManager):
   pass
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

server_addr= '127.0.0.1'
print('try to connect to %s' % server_addr)

m=QueueManager(address=(server_addr,5000),authkey=b'zq496547199')

m.connect()
task = m.get_task_queue()
result = m.get_result_queue()

for i in range(10):
   try:
      n=task.get(timeout=5)
      print('task get, run %d *%d' % (n,n))
      r = '%d * %d = %d' % (n,n, n*n)
      time.sleep(1)
      result.put(r)
   except task.Empty:
      print('task queue is empty.')
print('worker exit')
   
