# remove duplicate in string

str = "abbcddeff"
duplicate_string = []
unique_string = []

for i in str:
    if str.count(i) > 1:
        if i not in duplicate_string:
            duplicate_string.append(i)

print(duplicate_string)
unique_string = set(str) - set(duplicate_string)
print(list(unique_string))