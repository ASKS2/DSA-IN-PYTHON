#Here we have to take 3 numbers form the list and check if 
# their sum is equal to 0 or not. If it is equal 
# to 0 then we have to return the list of those 3 numbers.  

#brute force approach
arr = [-1, 0, 1, 2, -1, -4]
n = len(arr)
my_set=set()
for i in range(0,n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if arr[i]+arr[j]+arr[k]==0:
                my_set.add(tuple(sorted([arr[i],arr[j],arr[k]])))



#better approach
# here we will use the formula that arr[i]+arr[j]+arr[k]==0 => 
# arr[i]+arr[j]==-arr[k]
arr = [-1, 0, 1, 2, -1, -4]
n = len(arr)
my_set = set()
for i in range(n):
    for j in range(i+1, n):
        target = -(arr[i] + arr[j])
        if target in arr[j+1:]:
            my_set.add(tuple(sorted([arr[i], arr[j], target])))

print(list(my_set))


#optimal approach
# here we will use the two pointer approach.
#first we will sort the array and then we will fix one element and
# then we will use two pointer approach to find the other two elements.

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()

        for i in range(n):
            if i != 0 and nums[i] == nums[i - 1]:
                continue

            # moving the 2 pointers
            j = i + 1
            k = n - 1

            while j < k:
                total_sum = nums[i] + nums[j] + nums[k]

                if total_sum < 0:
                    j += 1

                elif total_sum > 0:
                    k -= 1

                else:
                    temp = [nums[i], nums[j], nums[k]]
                    ans.append(temp)
                    j += 1
                    k -= 1


                    