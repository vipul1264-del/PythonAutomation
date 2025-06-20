# List new Pattern


l = [1,3,5,7,3,"number", 9, 9 ,10, "SUMATION"]
l1 = list(set(l))
print(l1)
l2 = []
for i in l1:
    if isinstance(i, str):
        l2.append(i.swapcase())
    else:
        l2.append(i)
print(l2)
    