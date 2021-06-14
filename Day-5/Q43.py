# Q.43 A sparse matrix has many zero elements. 
# For example, the following 4x4 matrix is a sparse Matrix. 
# Conventional method of representation of such a matrix is not space efficient. 
# It will be prudent to store non-zero elements only. 
# If this is done, then the matrix may be thought of as an ordered list of non-zero elements. 
# Information about non-zero elements have three parts. Row, Column and its value.
# Examples:
# Input:
# 1 0 0 0
# 0 5 0 2
# 3 0 0 0
# 0 0 4 0
# Output:
# row	column	value
# 0	    0	  1 
# 1	    1	  5
# 1	    3	  2
# 2     0	  3
# 3	    2 	  4  
# Input:
# 1 0 0
# 0 5 0
# 0 0 0
# 0 0 6
# Output:
# row	column	value
# 0	    0	  1 
# 1	    1	  5
# 3	    2	  6
# note: you may assume row and column index starting from 0,0.

matrix = []
print('Enter list (one element at a time)')
while True:
    row = input("-> ")
    if not row: break
    matrix.append(list(map(int, row.split())))
print('row','| column','| value')

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j]:
            print(i,j,matrix[i][j],sep='       ')