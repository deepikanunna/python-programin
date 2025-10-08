# Create an array
arr = [10, 20, 20, 30, 10, 40, 50, 30]

# Remove duplicates manually
unique = []
for i in arr:
    if i not in unique:
        unique.append(i)

print("Original array:", arr)
print("Array after removing duplicates:", unique)
