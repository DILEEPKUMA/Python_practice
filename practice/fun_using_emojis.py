def emojis_func(message):
    words=message.split(' ')
    emojis_faces ={
        ":)": "😁",
        ":(": "😌"
    }
    result=""
    for word in words:
        result += emojis_faces.get(word,word) + " "
    return result


message=input("> ")
print(emojis_func(message))