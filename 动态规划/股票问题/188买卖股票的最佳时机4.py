#和股票问题3一样的思路，只是dp的列变多了
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = [[0]*(2*k+1) for _ in range(len(prices))]
        #初始化 dp偶数列是不持有， 奇数列是持有，
        for i in range(len(dp[0])):
            if i%2==1:
                dp[0][i] = -prices[0]
        #递归
        for i in range(1, len(prices)):
            for j in range(1, len(dp[0])):
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]+(-1)**j*prices[i])
        return dp[-1][-1]
