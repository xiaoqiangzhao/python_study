#! /home/b51816/Python-3.5.1/python

### Filter
def filter_loop_num(x):
   my_str = str(x)
   i = len(my_str)
   return my_str[:i//2] == my_str[-(i//2):][::-1]

my_list = [12345,12321,23642,82728,'abcdcba','ajfklw',702207,948273]    ## example

print(list(filter(filter_loop_num,my_list)))
