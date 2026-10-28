nums = [5,10,-3,-1,-10,6]
n = len(nums)
pos,neg = [],[]
for i in range(1,n):
  if nums[i]>=0:
    pos.append(i)
  else:
    neg.append(i)
    
for i in range(0,len(pos)):
  nums[2*i] = pos[i]
  nums[2*i + 1] = neg[i]
print(nums)
