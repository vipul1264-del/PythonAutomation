from abc import ABC, abstractmethod

class A(ABC):
    
    def show(self):
        print("Hello Abstract method")

    @abstractmethod
    def fun(self):
        pass

class B(A):
    def fun(self):
        print("fun 1")

class C(A):
    def fun(self):
        print("fun 2")

b = B()
b.show()
b.fun()

c = C()
c.show()
c.fun()


