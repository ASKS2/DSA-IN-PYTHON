#How to access the elements of a 2D matrix in Python
nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(0,len(nums)):
    for j in range (0,len(nums[0])):
                print(nums[i][j], end=", "  )