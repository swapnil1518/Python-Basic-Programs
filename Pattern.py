# Write a python program to print the following code
"""
*
**
***
****
*****
****
***
**
*

"""

def star(n):
  for i in range (n):
    for j in range(0,i+1):
      print("*", end="")
    print()
  for i in range(1,n):
    for j in range(i,n):
      print("*", end="")
    print()
n=5
star(n)