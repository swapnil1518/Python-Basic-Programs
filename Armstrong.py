#sum of cube of digits = digit itself

n = int(input("enter a number : "))
sum = 0
temp = n
while temp>0:
  digit =  temp%10
  digit = digit*digit*digit
  sum = sum + digit
  temp = temp//10
if n== sum:
  print("Armstrong")
else:
  print("Not Armstrog")
