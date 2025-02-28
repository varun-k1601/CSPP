matrix1=eval(input().strip())
matrix2=eval(input().strip())
def fun(matrix1,matrix2):
    if len(matrix1)!=len(matrix2):
        return False
    else:
        for i in range(len(matrix1)):
            for j in range(len(matrix1[i])):
                if len(matrix1[i]) != len(matrix2[i]):
                    return False
                if matrix1[i][j]!=matrix2[i][j]:
                    return False
    return True
print(fun(matrix1,matrix2))