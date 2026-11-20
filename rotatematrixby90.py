#this inculdes the brute force solution 
# to find the length of the longest 
# consecutive sequence in an unsorted 
# array of integers.

nums = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
jk=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
for i in range(len(nums)):
    for j in range(len(nums[0])):
        jk[i][j] = nums[len(nums)-1-j][i]
        
for i in range(len(jk)):
    for j in range(len(jk[0])):
        print(jk[i][j],end=" ")
    print()



#for the optimal solution first we will take the transpose then we will 
#try to convert the achevied matrix into the expected one

nums = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
for i in range(len(nums)):
    for j in range(i,len(nums[0])):
        nums[i][j],nums[j][i] = nums[j][i],nums[i][j]

print("after transpose")
for i in range(len(nums)):
    for j in range(len(nums[0])):
        print(nums[i][j],end=" ")
    print()


#now we just need to reverse the rows of the matrix to acheive 
# the expected output

for i in range(len(nums)):
    nums[i].reverse()

print("after 90 degree clockwise rotation")
for i in range(len(nums)):
    for j in range(len(nums[0])):
        print(nums[i][j],end=" ")
    print()