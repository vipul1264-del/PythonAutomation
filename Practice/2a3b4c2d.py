str = "aabbbccccddee"
count = 1
emp_list = []
pre_char = str[0]

for i in str[1:]:
    if i == pre_char:
        count = count + 1
    else:
        emp_list.append(f"{count}{pre_char}")
        pre_char = i
        count = 1

emp_list.append(f"{count}{pre_char}")

output = " ".join(emp_list)
print(output)
