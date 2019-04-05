matrix =[[1,2,3,[3,2,5]],
         [4,5,6],
         [7,8,9]]
print(matrix[0][3][2])



for column in matrix:
    for item in column:
        print(item)
