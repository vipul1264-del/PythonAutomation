class Parent:
    name = "vipul"

    def talk(self):
        print("Parent class can talk")


class Child():
    a = 8
    
    def sum(self):
        print(20+30)


class Lite(Parent, Child):
    b = 50

    def sub(self):
        print(100-27)


obj = Lite()
print(obj.name)
obj.talk()
obj.sum()              
