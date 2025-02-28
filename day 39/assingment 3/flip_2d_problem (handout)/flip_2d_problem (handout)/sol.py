l=eval(input())
def flip_2d_problem(l):
    l1=[]
    for i in l:
        l1.append(i[::-1])
    l1=l1[::-1]
    return l1
print(flip_2d_problem(l))