str1 = "abcd"
str2 = "acde"
l = []
for i in str1:
    if i not in str2:
        l.append(i)

print(l)

for i in str2:
    if i not in str1:
        l.append(i)

print(l)

output = ", ".join(l)
print(output)
print("***************second method*****************")
s3 = set(str1)
s4 = set(str2)
s5 = s3&s4
print(f"common element ::{s5}")
s6 = set(l) - set(s5)
print(f"uncommon element ::{s6}")

