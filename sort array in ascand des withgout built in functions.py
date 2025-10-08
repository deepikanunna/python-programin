# Create an array
arr = [45, 12, 78, 23, 56]

# Sort in ascending order (simple bubble sort)
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

print("Ascending order:", arr)

# Sort in descending order (simple bubble sort)
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

print("Descending order:", arr)
