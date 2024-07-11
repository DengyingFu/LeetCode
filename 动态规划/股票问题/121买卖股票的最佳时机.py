#===============快慢指针================
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        fast = slow = 0
        while fast<len(prices):
            lirun = prices[fast]-prices[slow]
            if lirun>=0:
                if lirun>res:
                    res = lirun
                fast += 1
            else:
                slow += 1      
        return res
#=============动态规划=====================
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0]*2 for _ in range(len(prices))]#dp[i][0]表示第i天持有股票的最大余额，dp[i][1]表示第i天不持有股票的最大余额
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], -prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]+prices[i])
        return max(dp[-1][0], dp[-1][1])
