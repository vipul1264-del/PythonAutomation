# common Letters In 2 List

l1 = [1,3,52,4,6,98,6]
l2 = [3,66,8,19,49,4]
cl = []

for a in l1:
    for b in l2:
        if a == b:
            cl.append(a)

print(cl)
