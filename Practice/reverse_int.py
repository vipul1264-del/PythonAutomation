# reverse integers

a=12345
r=0


while a>0:
    digit=a%10
    r = r*10+digit
   
    a = a//10

print(r)