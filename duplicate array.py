array = [1, 2, 3, 4, 1]
duplicate_array = [x for i, x in enumerate(array) if x not in array[:i]]
print(f"duplicate array={duplicate_array}")