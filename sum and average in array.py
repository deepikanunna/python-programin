# Create an array
arr = [10, 20, 30, 40, 50]

# Calculate sum without using built-in functions
total = 0
count = 0
for num in arr:
    total += num
    count += 1

# Calculate average
average = total / count

print("Sum of array elements:", total)
print("Average of array elements:", average)
