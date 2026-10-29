def maxProfit(prices):
    n = len(prices)
    maxprofit = 0

    for i in range(n - 1):
        for j in range(i + 1, n):
            profit = prices[j] - prices[i]
            maxprofit = max(maxprofit, profit)

    return maxprofit


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))