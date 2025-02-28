def is_magic_square(matrix):
    n = len(matrix)
    target_sum = sum(matrix[0])
    for row in matrix:
        if sum(row) != target_sum:
            return False
    for col in range(n):
        if sum(matrix[row][col] for row in range(n)) != target_sum:
            return False
    if sum(matrix[i][i] for i in range(n)) != target_sum:
        return False
    if sum(matrix[i][n - 1 - i] for i in range(n)) != target_sum:
        return False
    
    return True

matrix=eval(input())
print(is_magic_square(matrix))