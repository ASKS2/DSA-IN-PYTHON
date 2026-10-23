nums=[1,2,3,4,5,6,7,8,9,1,2,5,3,2,7,4,3,6,5,4,3,2,1,2,3,4,5,6,7,8,9]
freq_map={}
for i in range(1,len(nums)):
    if nums[i] in freq_map:
        freq_map[nums[i]] += 1