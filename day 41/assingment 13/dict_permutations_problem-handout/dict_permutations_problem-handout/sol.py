def are_dicts_equivalent(dict1, dict2):
    # Check if both dictionaries have the same number of values
    if len(dict1) != len(dict2):
        return False

    # Create sorted lists from values for comparison
    sorted_values1 = sorted([sorted(value) for value in dict1.values()])
    sorted_values2 = sorted([sorted(value) for value in dict2.values()])

    # Compare if the sorted lists match
    return sorted_values1 == sorted_values2
d1=eval(input())
d2=eval(input())
print(are_dicts_equivalent(d1, d2))