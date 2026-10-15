prices = [7,1,5,3,6,4]

n = len(prices)
max_profit = prices[0]
min_profit = 0

for i in range(0 , n):
    min_profit = min(min_profit , prices[i])
    max_profit = max(max_profit , (min_profit - prices[i]))
return max_profit


"""
time complexity is O(N)
space complexity is o (1)
"""
