# non repearting character

s = "geeksforgeeks"
str = set(s)
non_repeate_character = []
for i in str:
    if s.count(i) > 1:
        if i not in non_repeate_character:
            non_repeate_character.append(i)

print(non_repeate_character)

print("****************************************************************")

l = []
for i in s:
    if s.count(i) > 1:
        l.append(i)
print(l)
l1 = list(s)
l2 = list(set(l1) - set(l))
print(l2)
