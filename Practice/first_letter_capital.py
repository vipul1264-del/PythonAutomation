# first letter capital

s = "i love my india"
a = []
l = s.split()
print(l)

for i in l:   
    a.append(i[0].upper()+i[1:])
   
    
print(a)