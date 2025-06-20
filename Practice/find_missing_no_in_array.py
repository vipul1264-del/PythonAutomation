# find missinf number in an array

a = [1,2,3,4,5,6,7,8,10,11,12]
s = sum(a)
l = a[-1]

t = (l*(l+1))//2
mn = t-s
print(mn)