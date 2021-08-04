#!/bin/python3
# This code is for fibonacci series

num = int(input("Please Enter a range for fibonacci series "))
x = 1
y = 1
z = 0
i = 0
print(x,"\n",y)
while (i<=num):
  z = x + y
  print(z)
  x = y
  y = z
  i = i + 1
