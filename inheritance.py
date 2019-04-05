

class Parent_Class:
    def add(self):
        a=10
        b=20
        c=a+b
        print(f"sum of {a} and {b} = {c}")


class Child_Class1(Parent_Class):
    def child1(self):
        print("child class")


class Child_Class2(Child_Class1):
    def child2(self):
        print("child 2 class")


child= Child_Class1()
child.add()
child.child1()
child_1=Child_Class2()
child_1.child1()
cons.move()