# Original array
arr = [10, -5, 20, -30, 40, -2]

# Replace negative numbers with zero
for i in range(len(arr)):
    if arr[i] < 0:
        arr[i] = 0

print("Array after replacing negative numbers with zero:", arr)
