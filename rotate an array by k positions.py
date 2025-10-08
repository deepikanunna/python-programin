# Create an array
arr = [10, 20, 30, 40, 50]
k = 2  # Number of positions to rotate

# ----- Left Rotation -----
left_rotated = []
n = len(arr)
for i in range(n):
    left_rotated.append(arr[(i + k) % n])

print("Original array:", arr)
print(f"Array after {k} left rotations:", left_rotated)

# ----- Right Rotation -----
right_rotated = []
for i in range(n):
    right_rotated.append(arr[(i - k + n) % n])

print(f"Array after {k} right rotations:", right_rotated)
