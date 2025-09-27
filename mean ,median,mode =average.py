import statistics


numbers = [12, 45, 83, 52]


mean = statistics.mean(numbers)
median = statistics.median(numbers)
mode = statistics.mode(numbers)

average = (mean + median + mode) / 3

print("Average:", int(average))
