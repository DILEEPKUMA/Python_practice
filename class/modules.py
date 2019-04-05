class Persons:
    def __init__(self,name):
        self.name=name

    def talk(self):
        print(":)")
        print(f"hi ,mr {self.name}")


pers=Persons("john")
pers1=Persons("smith")
pers.talk()
pers1.talk()