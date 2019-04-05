phone =input("phone : ")
dict={
"1":"one",
"2":"two",
"3":"three",
"4":"four"
}
digits=""
for ch in phone:
    digits +=dict.get(ch) + " "

print(digits)