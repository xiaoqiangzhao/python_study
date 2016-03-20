#! /home/b51816/localpython/python3/bin/python3
from collections import namedtuple
from collections import deque
from collections import Counter
import hashlib
point = namedtuple('tri_point',('x','y','z'))
p1 = point(1,2,3)
print(p1)
print(p1.x,p1.y,p1.z)
print(Counter('zq496547199'))

md5 = hashlib.md5()
md5.update('jay is a shaby'.encode('utf-8'))
print(md5.hexdigest())
md5.update(", that's not ture".encode('utf-8'))
print(md5.hexdigest())
my_db = dict()
def md5_register(name,code):
   md5 = hashlib.md5()
   md5.update(code.encode('utf-8'))
   sha1 = hashlib.sha1()
   sha1.update(md5.hexdigest().encode('utf-8'))
   md5.update(sha1.hexdigest().encode('utf-8'))
   return md5.hexdigest()
my_name = input("Register Name:")
my_code = input("Register Password:")
my_db[my_name]= md5_register(my_name,my_code)
print(my_db)
log_name = input("Login in Name:")
log_pw = input("Password:")
if log_name in my_db:
   if md5_register(log_name,log_pw)==my_db[log_name]:
      print(md5_register(log_name,log_pw),my_db[log_name] )
      print("PASS")
   else:
      print("Invalid Password")
else:
   print("Invalid Log Name")
