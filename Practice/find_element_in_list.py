# find element in the list

l=[1,3,5,76,1,34,78,9]
n=76
f=0
for i in l:
    if i==n:
        f += 1
if f==1:
    print("yes")
else:
    print("no")