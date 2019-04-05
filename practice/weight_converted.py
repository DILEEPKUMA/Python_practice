weight  = int(input('enter the weight : '))
unit=input('(L)lbs and (K)kg :')

if unit.upper() == "L":
    converted=weight*0.45
    print(f"yur weight is :{converted}")
else:
    converted= weight/0.45
    print(f"yiur pounds is :{converted}")