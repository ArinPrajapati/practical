# Write a Python program to find the maximum subarray sum using Kadane's Algorithm.
def max_subarray_sum(arr):
    max_current = max_global = arr[0]
    for num in arr[1:]:
        max_current = max(num, max_current + num)
        if max_current > max_global:
            max_global = max_current
    return max_global

# Example usage:
arr = [-2, -3, 4, -1, -2, 1, 5, -3]
print("Maximum subarray sum is", max_subarray_sum(arr))