a = input("a: ")
b = input("b: ")

a,b = b,a
print(a,b)

 temp = a
 a = b
 b = temp
print(a,b)


