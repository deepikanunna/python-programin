# Program to find the average of positive and negative numbers

positive_sum = 0
positive_count = 0
negative_sum = 0
negative_count = 0

while True:
    num = int(input("Enter a number (-1 to stop): "))
    if num == -1:
        break
    elif num > 0:
        positive_sum += num
        positive_count += 1
    elif num < 0:
        negative_sum += num
        negative_count += 1

# Calculate averages safely
if positive_count > 0:
    avg_positive = positive_sum / positive_count
else:
    avg_positive = 0

if negative_count > 0:
    avg_negative = negative_sum / negative_count
else:
    avg_negative = 0

print("Average of positive numbers:", avg_positive)
print("Average of negative numbers:", avg_negative)