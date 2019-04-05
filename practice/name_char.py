name=input('enter your name :')
max_char=20
if len(name) < min_char:
    print("u r name  must be 3 char")
elif len(name) > max_char:
    print("u r name is must be 50 char maximum")
else:
    print('name is good')
