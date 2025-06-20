class Student:
    def _init__(self):
        self.__name = ""

    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name



obj = Student()
obj.setName("Vipul")
obj.getName