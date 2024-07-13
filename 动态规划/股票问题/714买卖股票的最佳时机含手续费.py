class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = [[0]*2 for _ in range(len(prices))]
        #初始化
        dp[0][0] = -prices[0]-fee
        dp[0][1] = 0
        #递推
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]-prices[i]-fee) #持有
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]+prices[i]) #不持有
        return dp[-1][1]
