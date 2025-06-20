# index value list

l = ['a', 'e', 'k', 'g', 'b']
index = 0
for i in l:
    print(index, i)
    index += 1


# second method
for index, i in enumerate(l):
    print(index, i) 