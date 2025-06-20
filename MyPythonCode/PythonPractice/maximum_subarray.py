# max_sub-array

a = [2,1,15,7,4,9,1,6,9]
print(a)
arr = sorted(a)
print(arr)

sub_arr = []
max_sum = 0

for i in range(len(arr)-1):
    current_sum = arr[i] + arr[i+1]

    if current_sum > max_sum:
        max_sum = current_sum
        sub_arr = [arr[i], arr[i+1]]

print(f"sub array is :: {sub_arr}")
print(f"max sum is :: {max_sum}")