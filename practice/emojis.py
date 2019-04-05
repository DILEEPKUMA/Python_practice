message=input("> ")
split=message.split(' ')
emojis={
    ":)": "😁",
    ":(": "😌"
}
empty_list=""
for messag in split:
    empty_list += emojis.get(messag,messag) + " "

print(empty_list)
print("🤣🤣🤣")