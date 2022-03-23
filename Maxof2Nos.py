n1 = int(input("enter 1st no : "))
n2 = int(input("enter 2nd no : "))
if n1>n2:
    print(n1,"is max")
else:
    print(n2,"is max")


#2nd way

def max(a,b):
    if a>b:
        return a
    else:
        return b
a=9
b=5
print(max(a,b))