# Create two arrays
arr1 = [10, 20, 30]
arr2 = [40, 50, 60]

# Merge arrays without using built-in functions
merged = []
for i in arr1:
    merged.append(i)
for j in arr2:
    merged.append(j)

print("First array:", arr1)
print("Second array:", arr2)
print("Merged array:", merged)
