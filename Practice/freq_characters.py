# frequency character

s="I love mangoes and mangoes love I"
l = s.split()
d={}

for i in l:
    if s.count(i)>0:
        if i not in d:
            d[i]=0
        d[i] +=1


print(d)