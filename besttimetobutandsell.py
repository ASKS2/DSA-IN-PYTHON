#Brute force approach to find the maximum profit from buying and selling a stock given the prices in the list 'nums'. The algorithm checks every possible pair of buy and sell days to calculate the profit and keeps track of the maximum profit found.
nums = [7, 2, 1, 5, 6, 4, 8]

n = len(nums)
maxprof = 0

for i in range(0, n):
    for j in range(i + 1, n):
        if nums[j] > nums[i]:
            p = nums[j] - nums[i]
            maxprof = max(maxprof, p)

print(maxprof)
