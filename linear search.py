# Create an array
arr = [10, 20, 30, 40, 50]

# Take element to search
x = int(input("Enter the element to search: "))

# Linear search
found = False
for i in range(len(arr)):
    if arr[i] == x:
        print(f"Element {x} found at index {i}")
        found = True
        break

if not found:
    print(f"Element {x} not found in the array")
