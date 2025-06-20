# monkey Patching

class test:
    def method(self):
        print("I am from the code")



def function():
    print("I am from the monkey function")


test.method = function

test.method()
# test.function()