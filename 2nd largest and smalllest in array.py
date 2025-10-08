# Create an array
arr = [12, 45, 7, 89, 23, 45]

# Initialize largest and second largest
if arr[0] > arr[1]:
    largest = arr[0]
    second_largest = arr[1]
else:
    largest = arr[1]
    second_largest = arr[0]

# Initialize smallest and second smallest
if arr[0] < arr[1]:
    smallest = arr[0]
    second_smallest = arr[1]
else:
    smallest = arr[1]
    second_smallest = arr[0]

# Traverse the array
for i in range(2, len(arr)):
    # For largest
    if arr[i] > largest:
        second_largest = largest
        largest = arr[i]
    elif arr[i] > second_largest and arr[i] != largest:
        second_largest = arr[i]

    # For smallest
    if arr[i] < smallest:
        second_smallest = smallest
        smallest = arr[i]
    elif arr[i] < second_smallest and arr[i] != smallest:
        second_smallest = arr[i]

print("Second largest element:", second_largest)
print("Second smallest element:", second_smallest)
