# Create a program to sort a list of tuples based on the second element.

def sort_list_of_tuples(lst: list[tuple]):
    return sorted(lst, key=lambda x: x[0])
                                    #  | is this index of element in tuple


print(sort_list_of_tuples([(1, 2), (3, 1), (5, 3), (4, 4), (2, 5)]))