# Create an array
arr = [12, 45, 7, 89, 23]

# Assume first element is both max and min
max_num = arr[0]
min_num = arr[0]

# Find max and min using a loop
for num in arr:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

print("Maximum element:", max_num)
print("Minimum element:", min_num)
