# Original array
arr = [2, 4, 3, 5, 7, 8, 1]

# Target sum
target = 7

# Find pairs
print(f"Pairs with sum {target}:")
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            print(f"({arr[i]}, {arr[j]})")
