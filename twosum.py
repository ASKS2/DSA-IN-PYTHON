nums = [5,9,1,2,4,15,6,3]
n = len(nums)
for i in range(0,n):
  for j in range(0,i):
    if nums[i]+nums[j]==13:
      print(f"Numbers are {nums[i]} and {nums[j]}")
    