a=eval(input())
def fun(a):
    if len(a)==0:
        return [[]]
    else:
        max_row=0
        max_col=0
        for (i,j) in a.keys():
            if i>max_row:
                max_row=i
            if j>max_col:
                max_col=j
        l=[]
        for i in range(max_row+1):
            row=[]
            for j in range(max_col+1):
                row.append(0)
            l.append(row)
        for (i,j), value in a.items():
            l[i][j]=value
    return l
print(fun(a))