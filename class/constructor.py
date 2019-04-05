class Constructor:
    def move(self):
        print("move")

    def __init__(self,x,y):
        self.x=x
        self.y=y

cons = Constructor(10,20)
cons.move()
print(cons.x)
print(cons.y)

