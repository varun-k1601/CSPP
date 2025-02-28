a=eval(input())
def group_strings_problem(a):
    d={}
    for i in a:
        first=i[0]
        if first not in d:
            d[first]=[i]
        else:
            d[first].append(i)
    return d
print(group_strings_problem(a))
