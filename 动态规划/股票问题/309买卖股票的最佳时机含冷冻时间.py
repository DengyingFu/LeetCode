class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0]*4 for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        for i in range(1, len(prices)):
            tmp = max(dp[i-1][1]-prices[i], dp[i-1][3]-prices[i])
            dp[i][0] = max(dp[i-1][0], tmp) #持有
            dp[i][1] = max(dp[i-1][1], dp[i-1][3]) #冷冻后不持有
            dp[i][2] = dp[i-1][0] + prices[i] #卖出
            dp[i][3] = dp[i-1][2] #冷冻
        return max(dp[-1])
