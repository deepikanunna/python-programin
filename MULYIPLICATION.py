# Take input from user
A = int(input("Enter the number: "))
B = int(input("Enter the range: "))

# Display multiplication table
for i in range(1, B + 1):
    print(f"{A} x {i} = {A * i}")
