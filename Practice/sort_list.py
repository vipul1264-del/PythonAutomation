# sort list

l=[11,14,52,43,78,0,99,5]
n=len(l)
l2=sorted(l)
print(f"I am from sorted method {l2}")

for i in range(0, n):
    for j in range(i+1, n):
        if l[i]>l[j]:
            l[i], l[j] = l[j], l[i]

print(l)