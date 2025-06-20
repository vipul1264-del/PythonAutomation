class A:

    __status = "Active"

    def __init__(self):

        self._name = "name"
    
    def _show(self):
        print("show")
    
    def _value(self, value):
        self.value = value
        print(value)
    
    print(__status)

class B(A):
    def __init__(self):
        A.__init__(self)
        print(self._name)

b = B()
b._value("value")
b._show()
print(b.__status)
        
    







