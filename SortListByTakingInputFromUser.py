a = []
# print(type(a))
for i in range(5):
    x = input("enter element of list : ")    # taking list element from user
    a.append(x)   # addding x elements in the list a
print("Original list", a)
a.sort()        # sortig the values
print("New list",a)


