import statistics

# Write a Python script to calculate statistics (mean, median, mode) using the statistics module.
data = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9]

mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)

print(f"Mean: {mean}")
print(f"Median: {median}")    
print(f"Mode: {mode}")
