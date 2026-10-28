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

#Optimal solution using a single pass approach
min_price = nums[0]
max_profit = 0

for price in nums[1:]:
    if price < min_price:
        min_price = price
    elif price - min_price > max_profit:
        max_profit = price - min_price

print(max_profit)