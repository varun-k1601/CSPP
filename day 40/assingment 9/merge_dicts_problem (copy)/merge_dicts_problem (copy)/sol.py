d1=eval(input())
d2=eval(input())
d3={**d1,**d2}
def fun(d1,d3):
    for key in d1.keys():
        if key in d2:
            d3[key]=d1[key]+d2[key]
    return d3
print(fun(d1,d3))