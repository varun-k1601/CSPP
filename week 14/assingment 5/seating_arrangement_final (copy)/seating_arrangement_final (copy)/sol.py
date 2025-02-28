l=eval(input())
def fun(l):
    max1=float('-inf')
    curr_max=0
    for i in l:
        curr_max=0
        for char in i:
            if char=='O':
                max1=max(max1,curr_max)
                curr_max=0
            elif char=='E':
                curr_max+=1
        max1=max(curr_max,max1)
    return max1
print(fun(l))
# ['OOEEEOO', 'EEEOOOOO', 'OOOOEEEO']