 # armstrong number

n=407
l=len(str(n))
temp=n
sum=0

while temp>0:
    digit=temp%10
    sum=sum+digit**l
    temp = temp//10

if sum==n:
    print("armstrong")
else:
    print("not an armstrong")
