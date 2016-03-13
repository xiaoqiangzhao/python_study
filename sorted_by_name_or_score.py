#! /home/b51816/Python-3.5.1/python
### sorted
L = [('jay',100),('qqq',20),('xiaozhe',101),('taozhong',99),('xiaowu',44)]

def get_name(t):
   return t[0]
def get_score(t):
   return t[1]
print(sorted(L,key=get_name))
print(sorted(L,key=get_score,reverse=True))
