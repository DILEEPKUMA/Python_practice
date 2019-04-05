list=[]
for x in range(10,100):
    if(x%7==0) and (x%5==0):
        list.append(str(x))
print(','.join(list))