#  fibonnacci series  0,1,1,2,3,5,8,13,21,34......

n1=0
n2=1
sum=0
for i in range(2, 10):
    sum=n1+n2
    print(sum)
    n1=n2
    n2=sum

