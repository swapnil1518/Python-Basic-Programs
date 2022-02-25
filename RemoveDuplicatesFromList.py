# to remove duplicates from a list we will convert list into set because set is acollection of unique elemnts and then
#again convert output set into lis

l1 = ['1','2','2','3','4','5','6','6','7','8']
se = set(l1)
print(se)
li = list(se)
print(li)
