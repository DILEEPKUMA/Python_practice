numbers=[5,2,5,2,2]
for i in numbers:
    print("X" * i)

num1=[1,2,3,4,5,4,3,2,1]
for i in num1:
    print("*" * i)


num2=[5,2,5,2,2]
for x_count in num2:
    empty_list=''
    for count in range(x_count):
        empty_list += 'X'
    print(empty_list)
