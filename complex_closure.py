#! /home/b51816/Python-3.5.1/python
def compose_h (f,g):
   def h(x):
      return f(g(x))
   return h
def b(x):
   return x**2 + x**3
def d(x):
   print ("g(x) is",x+2)
   return x+2
add_and_square = compose_h(b,d)
print (add_and_square(1))
