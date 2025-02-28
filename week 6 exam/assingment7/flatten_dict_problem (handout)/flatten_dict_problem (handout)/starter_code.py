# d1=eval(input())
# d2={}
# s4=''
# l=[]
# def fun(d1):
#     global s4
#     for key,value in d1.items():
#         if type(value)==dict:
#             l.append(key)
#             return fun(value)
#         elif type(value)!=dict and len(l)==0:
#             d2[key]=value
#         elif len(l)>0:
#             if type(value)!=dict:
#                 s4='.'.join(l)
#                 d2[s4]=value
#                 l.clear()
#     return d2
# print(fun(d1))
# {"a": 1, "b": {"c": 2, "d": {"e": 3}}}
# {'a': 1, 'b.c': 2, 'b.d.e': 3}
a=eval(input())
d1={}
s1=''
l=[]
def fun(a):
    for key,value in a.items():
        if type(value)==dict:
            l.append(key)
            fun(value)
            l.remove(key)
        elif type(value)!=dict and len(l)==0:
            d1[key]=value
        elif len(l)>0:
            if type(value)!=dict:
                l.append(key)
                s1='.'.join(l)
                d1[s1]=value
                l.remove(key)
                s1=''
    return d1
print(fun(a))
#{"x": {"y": {"z": 1}}, "a": 2}
#{'x.y.z': 1, 'a': 2}