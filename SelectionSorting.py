def selection_sort(num):
    for i in range(5):
        min_pos = i
        for j in range(i,6):
            if num[j]<num[min_pos]:
                min_pos=j
        temp = num[i]
        num[i]= num[min_pos]
        num[min_pos]=temp
       # print(num) # to check iteration total iteration is 6
num = [5,3,8,6,7,2]
selection_sort(num)
print(num)


# for i in range(5): -> since dealing with inimum value and fixing minimum value at the 1st postion.
# min_pos =i fixing min value
# inner loop - j in range(i,6) since we are reducing the size of array everytime so in range i to 6 till last last element
# min pos = j -> defining the min value  when we get new min value which is samller than
# while min_pos:
#swaping for outer loop, to make 1 swap for 1 iteration

