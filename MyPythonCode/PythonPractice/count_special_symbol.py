
# count_special_symbol

s = "a!@123dh^kjhk*646GJhg%4^*f*&"
l = len(s)
n = 0
c = 0
for i in s:
    if i.isdigit():
        n += 1
    elif i.isalpha():
        c += 1

sc = l-(n+c)
print(sc)



