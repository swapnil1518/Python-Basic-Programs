# Write a Python program to find the sum of all items in a dictionary
# 1st way
d1 = {'a': 200, 'b':300, 'c':400}
print("sum of values is : ", sum(d1.values()))

#2nd way
d2 = {'math':80, 'science':70, 'english':60, 'Computer':50}
sum = 0
for i in d2.values():
    sum = sum+i
print("sum of all subjects marks : ", sum)