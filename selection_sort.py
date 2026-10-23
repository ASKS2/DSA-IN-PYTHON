def mini_ind(nums):
  n = len(nums)
  for i in range(0,n):
    mini_index=i
    for j in range(0,n):
      if nums[j]<nums[mini_index]:
        mini_index = j
    nums[i],nums[mini_index]=nums[mini_index],nums[i]
    