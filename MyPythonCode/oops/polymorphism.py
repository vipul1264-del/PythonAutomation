class Parent:
    name = "parent"

    def show(self):
        print("parent")


class Child(Parent):
     name = "child"
     def show(self):
         Parent.show(self)
         super().show()
         print("child")

p = Parent()
p.show()
c = Child()
c.show()

