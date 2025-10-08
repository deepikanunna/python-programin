# Create an array
arr = [10, 20, 10, 30, 20, 10]

# Count frequency manually
for i in range(len(arr)):
    count = 0
    # Skip already counted elements
    if arr[i] != -1:
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count += 1
                # Mark duplicate as counted
                if i != j:
                    arr[j] = -1
        print(f"Element {arr[i]} occurs {count} times")
