d1=eval(input())
d2=eval(input())
d3={**d1,**d2}
def fun(d1,d3):
    for key,value in d3.items():
        if key in d1 and key in d2:
            d3[key]=d1[key]+d2[key]
    return d3
print(fun(d1,d3))
# {'name': 'John', 'age': 30}
# {'name': 'Doe', 'age': 25}