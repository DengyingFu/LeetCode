class Solution:
    def numSquares(self, n: int) -> int:
        #物品是数字m的平方，求背包容量为n最少能由多少个物品装满
        m = n
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        for i in range(1, int(n**0.5)+1): #遍历物品
            for j in range(i*i, n+1): #遍历背包
                dp[j] = min(dp[j], dp[j-i*i]+1)
        return dp[n] if dp[n]!=float('inf') else n
