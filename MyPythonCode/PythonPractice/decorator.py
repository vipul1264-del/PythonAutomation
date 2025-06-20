# decorator function

def decorator(func):
    print("Hello")
    func()
    print("thanks for using decorator function")

    return decorator

def main_function():
    print("Vipul Singh")

obj = decorator(main_function)