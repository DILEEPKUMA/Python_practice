import random

# for i in range(3):
#     print(random.randint(10,20))

members =["a","b","c","d","e"]
leaders=random.choice(members)
print(leaders)


class Dice():
    def roll(self):
        first=random.randint(1,6)
        second=random.randint(1,6)
        return first,second


dic=Dice()
print(dic.roll())


