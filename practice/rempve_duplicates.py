list=[1,2,2,4,5,3,3,7,8,6]
empty_list=[]
for num in list:
    if num not in empty_list:
        empty_list.append(num)
print(empty_list)