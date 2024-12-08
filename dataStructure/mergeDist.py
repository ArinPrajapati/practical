# Write a Python script to merge two dictionaries.


def merge_two_dicts(dict1: dict, dict2: dict):
    return {**dict1, **dict2}


dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

print(merge_two_dicts(dict1, dict2))