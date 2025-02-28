a=eval(input())
def most_popular_person(a):
    max=0
    for key,value in a.items():
        b=len(value)
        if b>max:
            max=b
            c=key
    return c
print(most_popular_person(a))
