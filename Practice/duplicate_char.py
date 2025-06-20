# duplicat characters

s="dasajh"
d={}
for i in s:
    if s.count(i)>1:
        if i not in d:
            d[i]=0
        d[i] += 1

print(d)