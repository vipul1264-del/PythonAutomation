# 3a4b2c5d1e

s = "aaabbbbccddddde"
count = 0
l = [] 
pre_char = s[0]

for i in s:
    if i == pre_char:
        count += 1
    else:
        l.append(f"{count}{pre_char}")
        count = 1
        pre_char = i

l.append(f"{count}{pre_char}")

output = "".join(l)
print(output)
