a=eval(input())
d={}
def fun(a):
    for word in a:
        first_letter=word[0]
        if first_letter not in d:
            d[first_letter]=[]
        d[first_letter].append(word)
    return d
print(fun(a))
# ['apple', 'banana', 'cherry', 'avocado', 'blueberry', 'carrot']
# {'a': ['apple', 'avocado'], 'b': ['banana', 'blueberry'], 'c': ['cherry', 'carrot']}