# repeated non repeated list

num = [1,1,2,3,4,2,5,6,7,8,6,1,2,3,9]
 
# repeated list : [1, 2, 3, 6]
# non repeated list : [4, 5, 7, 8, 9]  
r = []
nr = []

for i in num:
    if num.count(i) > 1:
        r.append(i)
        

r2 = set(r)
repeater_list = list(r2)
print(repeater_list)
non_repeater_list = []

for i in num:
    if num.count(i) > 0:
        if i not in repeater_list:
            non_repeater_list.append(i)

print(non_repeater_list)