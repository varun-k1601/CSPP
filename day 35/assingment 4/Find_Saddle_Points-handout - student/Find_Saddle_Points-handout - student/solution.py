def find_saddle_points(matrix):
    n = len(matrix)
    saddle_points = []
    for i in range(n):
        row = matrix[i]
        min_value = min(row)
        min_indices = [j for j, value in enumerate(row) if value == min_value]
        for j in min_indices:
            column = [matrix[k][j] for k in range(n)]
            if min_value == max(column):
                saddle_points.append((i, j))
    if saddle_points:
        return saddle_points
    else:
        return "No saddle point."
a=eval(input())
print(find_saddle_points(a))
