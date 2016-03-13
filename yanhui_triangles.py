#! /home/b51816/Python-3.5.1/python

### dumb method, operate element in the list
def yanhui(n):
   i = 1
   c_list = [1]
   next_list = [1]
   while i <=n:
      yield c_list
      i = i+1
      for index in range(i-1):
         # print(i,range(i-1))
         if index == i-2:
            next_list.append(1)
         else:
            next_list.append(c_list[index]+c_list[index+1])
      c_list = next_list
      next_list = [1]
   return "done"

# yanhui(5)
# for n in yanhui(7):
   # print(n)
   
### much  smarter method, take list as operator
def triangles():
   L = [1]
   yield L
   while True:
      L = [1] +[L[i]+L[i+1] for i in range(len(L)-1)] + [1]
      yield L


for l in triangles():
   print(l)
   if len(l) == 10:
      break
