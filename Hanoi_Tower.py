#! /home/b51816/Python-3.5.1/python

### HAN NUO Tower
def move(n,a,b,c):
   if n==1 :
      print(a,"-->",c)
   else:
      move(n-1,a,c,b)
      move(1,a,b,c)
      move(n-1,b,a,c)

A = 'A'
B = 'B'
C = 'C'
move(4,A,B,C)  ## exmaple for hanoi tower
