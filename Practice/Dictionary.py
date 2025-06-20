# Dictionary

d = {
    "ram" : {
        "rn" : 10, 
        "age" : 36, 
        "city": {
            "temp" : "dehradun",
            "perm" : {
                "local" : "abc",
                "pin" : [1,2,3]

            }
        } },

        "ram" : {
        "rn" : 10, 
        "age" : 36, 
        "city": {
            "temp" : "dehradun",
            "perm" : {
                "local" : "abc",
                "pin" : [1,2,3]

            }
        } }
}

print(d)
print(d["ram"]["city"]["perm"]["pin"])
d["ram"]["city"]["hobby"] = "travelling"
print(d)

print(d)

my_dict = {'a': 1, 'b': 2, 'c': 3}
list_of_keys = list(my_dict.keys())
list_of_values = list(my_dict.values())
print(list_of_keys)  # Output: ['a', 'b', 'c']
print(list_of_values) # Output: [1, 2, 3]

my_dict = {'a': 1, 'b': 2, 'c': 3}
list_of_tuples = list(my_dict.items())
print(list_of_tuples)  # Output: [('a', 1), ('b', 2), ('c', 3)]

print('_'*100)

dic = {
    'name' : 'vipul',
    'company' : 'iris software',
    'city' : 'noida',
    'profile' : 'senior tester'
}

print(dic)

for i in dic:
    print(i)

print('_'*100)

for i in dic:
    print(dic[i])

print('_'*100)

for i in dic.items():
    print(i)

print('_'*100)

for i in dic.keys():
    print(i)

print('_'*100)

for i in dic.values():
    print(i)