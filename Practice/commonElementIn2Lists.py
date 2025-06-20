# common letter in two string

l1 = [1,3,7,8,0,2]
l2 = [5,3,7,6,8,1]
l3 = []

for i in l1:
    for j in l2:
        if i == j:
            l3.append(i)

print(l3)
