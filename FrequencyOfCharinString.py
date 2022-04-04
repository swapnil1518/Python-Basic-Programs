s = input("enter a string : ")
c = input(" eneter a char whose frequency you want to check: ")
count = 0
for i in s:
    if i ==c:
        count += 1
print(c, "occurs", count, "times")