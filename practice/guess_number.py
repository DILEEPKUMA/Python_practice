secretno=8
guess_count=0


while guess_count < 3:
    user_no=int(input("your no :"))
    guess_count=guess_count+1
    if user_no==secretno:
        print("well done")
        break
    else:
        print("sorry try again")

print("chance overe")