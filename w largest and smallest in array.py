# Create an array
arr = [12, 45, 7, 89, 23]

# Initialize largest and smallest
largest = arr[0]
smallest = arr[0]

# Traverse the array to find largest and smallest
for num in arr:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

# Calculate difference
difference = largest - smallest

print("Largest element:", largest)
print("Smallest element:", smallest)
print("Difference between largest and smallest:", difference)
