# l = [3,5,6,3,9,0,3,8,3,1,3]. Print highest occurrence no in a list

l = [3,5,6,3,9,0,3,8,3,1,3]
new_list = []
count = 0
for i in l:
    new_list = [i]
    if i in new_list:
        count +=1
print(new_list)

