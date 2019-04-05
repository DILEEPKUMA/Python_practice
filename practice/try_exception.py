try:
    age =int(input("AGE : "))
    sales= 2000
    total=sales/age
    print(age,total)
except ZeroDivisionError:
    print("the age is not 0...")
except ValueError:
    print("invalid entry")