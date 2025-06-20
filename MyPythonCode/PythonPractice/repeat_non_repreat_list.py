full_list = [1,3,4,1,4,3,7,5,2,9,3,7]
print(f"full list :: {full_list}")
reperated_list = []
for i in full_list:
    if full_list.count(i) > 1:
        if i not in reperated_list:
            reperated_list.append(i)
        
print(f"Repeated list :: {reperated_list}")

non_repeated_list = list(set(full_list) - set(reperated_list))
print(f"non repeated list :: {non_repeated_list}")