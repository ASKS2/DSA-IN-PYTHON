#find the largest number in array/list:
nums= [55, 32, -97, 99, 3, 67 ]
largest = nums[0]
for i in range(1,len(nums)):
  if nums[i]>largest:
    largest = nums[i]

print(largest)

#for writing minus infinity we write float("-inf")