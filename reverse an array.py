# Create an array
arr = [10, 20, 30, 40, 50]

# Reverse the array manually
rev = []
for i in range(len(arr) - 1, -1, -1):
    rev.append(arr[i])

print("Original array:", arr)
print("Reversed array:", rev)
