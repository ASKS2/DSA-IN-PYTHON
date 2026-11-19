#How to access the elements of a 2D matrix in Python
nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(0,len(nums)):
    for j in range (0,len(nums[0])):
                print(nums[i][j], end=", "  )



# How to print the lower triangle matrix of a 2D matrix in Python

nums = [[5,10,8],[7,6,3],[2,1,9]]
for i in range(0,len(nums)):
        for j in range (0,len(nums[0])):
                        if i<j:
                            print("*", end=" ")
                        else:
                            print(nums[i][j], end=" ")

        print()



#How to print the upper triangle matrix of a 2D matrix in Python

nums = [[5,10,8],[7,6,3],[2,1,9]]
for i in range(0,len(nums)):
        for j in range (0,len(nums[0])):
                        if i>j:
                            print("*", end=" ")
                        else:
                            print(nums[i][j], end=" ")

        print()


# Transpose of a 2D matrix in Python

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rows = len(matrix)
cols = len(matrix[0])

transpose = []

for j in range(cols):
    new_row = []
    for i in range(rows):
        new_row.append(matrix[i][j])
    transpose.append(new_row)

for row in transpose:
    print(row)