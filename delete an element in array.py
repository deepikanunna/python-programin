# Original array
arr = [10, 20, 30, 40, 50]

# Element to delete
element = 30

# Create a new array without the element
new_arr = []
for i in arr:
    if i != element:
        new_arr.append(i)

print("Original array:", arr)
print(f"Array after deleting {element}:", new_arr)
