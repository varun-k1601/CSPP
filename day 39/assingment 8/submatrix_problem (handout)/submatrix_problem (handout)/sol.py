def contains_submatrix(matrix, submatrix):
    
    rows_matrix = len(matrix)
    cols_matrix = len(matrix[0])
    rows_submatrix = len(submatrix)
    cols_submatrix = len(submatrix[0])

   
    for i in range(rows_matrix - rows_submatrix + 1):
        for j in range(cols_matrix - cols_submatrix + 1):
           
            match_found = True
            
            for x in range(rows_submatrix):
                for y in range(cols_submatrix):
                    if matrix[i + x][j + y] != submatrix[x][y]:
                        match_found = False
                        break
                if not match_found:
                    break
            
           
            if match_found:
                return True
                
    
    return False
matrix=eval(input())
submatrix=eval(input())

print(contains_submatrix(matrix, submatrix))