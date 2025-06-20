l = [18,23,67,12,19,31,65,2,9,10,52]

min=l[0]
max=l[0]

for i in l:
    if i>max:
        max = i

print(max)

for i in l:
    if i<min:
        min=i

print(min)
