def create_spiral_matrix(nums, n):
    # Initialize an empty n x n matrix filled with zeros
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    
    # Define the boundaries for the spiral traversal
    top, bottom = 0, n - 1
    left, right = 0, n - 1
    
    # Index to keep track of elements in the nums list
    index = 0
    
    # Fill the matrix in a spiral order
    while top <= bottom and left <= right:
        # Fill the top row from left to right
        for i in range(left, right + 1):
            matrix[top][i] = nums[index]
            index += 1
        top += 1
        
        # Fill the right column from top to bottom
        for i in range(top, bottom + 1):
            matrix[i][right] = nums[index]
            index += 1
        right -= 1
        
        # Fill the bottom row from right to left
        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = nums[index]
                index += 1
            bottom -= 1
        
        # Fill the left column from bottom to top
        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = nums[index]
                index += 1
            left += 1
    
    return matrix
nums=eval(input())
n=int(input())
print(create_spiral_matrix(nums,n))