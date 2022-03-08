li = [5,6,7,3,1,8,4,2]
print("original list",li)
#print(type(li))
li.sort()
print("sorted list",li)

# Note : if you are storing li.sort() in avariable and then trying to print the variable. The result will be none because
# sort function just do the sorting it won't creating any copy of sorted values
# so new_list = li.sort() the print(new_list) -> O/p is None
