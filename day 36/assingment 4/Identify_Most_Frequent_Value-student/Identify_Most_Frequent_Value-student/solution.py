a=eval(input())
def fun(a):
    frequency = {}
    for values in a.values():
        for value in values:
            if value in frequency:
                frequency[value] += 1
            else:
                frequency[value] = 1
    min=float('-inf')
    for key, value in frequency.items():
        if value>min:
            min=value
            most_frequent=key
    return most_frequent
print(fun(a))
# {'a': [1, 2, 3], 'b': [3, 4, 5], 'c': [1, 3, 6]}
# 3