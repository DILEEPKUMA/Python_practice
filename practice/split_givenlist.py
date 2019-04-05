#Write a Python program that prints each item and its corresponding
# type from the following list.
#Sample List : datalist = [1452, 11.23, 1+2j, True,
# 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

for item in datalist:
    print("type item",item,"is ", type(item))


# print(type(datalist[0]))
# print(type(datalist[1]))
# print(type(datalist[2]))
# print(type(datalist[4]))
# print(type(datalist[5]))
# print(type(datalist[6]))
# print(type(datalist[7]))
# print(type(datalist[7]["section"]))
