#Brute force solution

def missingNumber(nums):
    for i in range(1, len(nums) + 2):
        if i not in nums:
            return i


#optimal solution 

def missingNumber(nums):
    n = len(nums)
    freq = {}
    for i in range(0, n + 1):
        freq[i] = 0


    for num in nums:
        freq[num] = 1

 
    for k, v in freq.items():
        if v == 0:
            return k


nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(missingNumber(nums))
