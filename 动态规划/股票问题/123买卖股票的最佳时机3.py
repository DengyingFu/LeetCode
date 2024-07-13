class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0]*5 for _ in range(len(prices))]#dp[i][0]表示无操作，[1]第一次持有，[2]第一次不持有，[3]第二次持有，[4]第二次不持有
        dp[0][1] = -prices[0] 
        dp[0][3] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
            dp[i][2] = max(dp[i-1][2], dp[i-1][1]+prices[i])
            dp[i][3] = max(dp[i-1][3], dp[i-1][2]-prices[i])
            dp[i][4] = max(dp[i-1][4], dp[i-1][3]+prices[i])
        return dp[-1][4]
