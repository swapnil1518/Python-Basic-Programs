def Remove(duplicate):
    final_list = []   # created temporays list to store nos 1 by 1
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list


# Driver Code
duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
print(duplicate)
print(Remove(duplicate))