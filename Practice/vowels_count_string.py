# vowels count in string

s = "amita"
l = []

for i in s:
    if i == 'a':
        l.append(i)
    elif i == 'e':
        l.append(i)
    elif i == 'i':
        l.append(i)
    elif i == 'o':
        l.append(i)
    elif i == 'u':
        l.append(i)

print(l)
d = {}
for i in l:
    if l.count(i) > 0:
        if i not in d:
            d[i] = 0
        d[i] +=1

print(d)