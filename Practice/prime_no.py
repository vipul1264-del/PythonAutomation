# prime number

n = 23
f = 0

for i in range(2, n+1):
    if n%i==0:
        f += 1

if f==1:
    print("prime")
else:
    print("not a prime")