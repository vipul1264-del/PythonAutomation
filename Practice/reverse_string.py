# reverse string

s="vipul"
s1=s[::-1]
print(s1)

###################################################

s1="my name is vipul singh"
s2=s1[::-1]
print(s2)

####################################################

str="my name is vipul singh"
l=str.split()
r=[]
for i in l:
    r.append(i[::-1])

print(r)

res=" ".join(r)
print(res)