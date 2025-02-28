def rotate_matrix_90_left(matrix, col=0):
   
    if col == len(matrix[0]):
        return []

    new_row = [matrix[i][col] for i in range(len(matrix) - 1, -1, -1)]

    return [new_row] + rotate_matrix_90_left(matrix, col + 1) 


matrix =eval(input())

result = rotate_matrix_90_left(matrix)
print(result)