# Write a Python program to find the largest and smallest elements in a list.

def find_largest_and_smallest_elements_in_list(lst:list[int]):
    largest = lst[0]
    smallest = lst[0]
    for i in lst:
        if i > largest:
            largest = i
        if i < smallest:
            smallest = i
    return largest, smallest
    
print(find_largest_and_smallest_elements_in_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))