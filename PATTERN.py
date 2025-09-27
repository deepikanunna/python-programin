# Take input from user
ch = input("Enter the Character to be printed: ")
rows = int(input("Number of rows: "))

# Print the pattern
for i in range(1, rows + 1):
    print((ch + " ") * i)
