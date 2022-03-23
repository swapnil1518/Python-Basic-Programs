start_range = int(input("enter starting range : "))
end_range = int(input("enter end range : "))
print("prime no in the range", start_range, "to", end_range)
for i in range(start_range,end_range+1):
    flag = 0                                            #flag = 0 assuming the no is prime. if assuming no is not prime then set flag =1
    for j in range(2,i):                                # take i as 1 no then check from 2 to i is divisible by o
        if (i%j==0):
            flag =1
            break     # if no is divisible by any of the no no need to check further
    if (flag ==0):
        print(i,end= ' ')
