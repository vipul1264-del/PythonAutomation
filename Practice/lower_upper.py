a="aBCdeE HgtU JiKoNEgc "
b=""

for i in a:
    if i.isupper()==True:
        b += i.lower()

    elif i.islower()==True:
        b += i.upper()

    elif i.isspace()==True:
        b += i

print(b) 