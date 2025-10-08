# Create an array
arr = [10, 20, 30, 40, 50, 60]

# Find the middle index
n = len(arr)
mid = n // 2

# Split the array
first_half = []
second_half = []

for i in range(mid):
    first_half.append(arr[i])

for i in range(mid, n):
    second_half.append(arr[i])

print("Original array:", arr)
print("First half:", first_half)
print("Second half:", second_half)
