# num = [5,3,8,6,7,2]
# num.sort()
# print(num)

def Bubble_Sort(num):                    # creating our own sort function. This function is taking num which is list as parmeter
    for i in range (len(num)-1,0,-1):
        for j in range(i):
            if num[j]>num[j+1]:  #5>3 T then swap else no
                temp = num[j]
                num[j]= num[j+1]
                num[j+1]= temp
num = [5,3,8,7,2]
Bubble_Sort(num)
print((num))


 #for i in range (len(num)-1,0,-1):
# outer loop for no of iteration. Suppose length is 6 then len(num
# len(num)-1 = 5 to 0 means iteration will be atleast 5 times. i.e for 6 elemts iteration will 5 times to check each elements
# -1 means iteration is backwards

#  for j in range(i):
# this inner loop is for comarision and swapping. we are fixing 1 value at end of every iteration
#     # so it will go till i times means for 1st iteration j=5 then inner loop will move 5 timeas and fix 1 largest elemnet
#     # at the end the agian in next iteration i =4 so it will move/swap 4 times and again fix 2nd largest elemebt