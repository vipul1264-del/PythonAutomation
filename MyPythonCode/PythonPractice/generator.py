# generators

def gen(n):
    while n > 0:
        yield n
        n -= 1
x = gen(5)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
    