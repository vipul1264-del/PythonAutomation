# frequency word

s="i love kavita and kavita love i"
l=s.split()
d={}
for i in l:
    if l.count(i)>0:
        if i not in d:
            d[i] = 0
        d[i] = d[i] + 1

print(d)