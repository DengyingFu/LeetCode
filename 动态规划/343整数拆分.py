class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0]*(n+1)  #dp[i]含义：数i拆分后所能获得的最大乘积
        dp[0] = dp[1] = 0
        dp[2] = 1  
        for i in range(3, len(dp)): #从dp[3]开始
            for j in range(1, i//2+1): #i拆分为j和i-j，或j和dp[i-j]
                dp[i] = max(j*(i-j),j*dp[i-j], dp[i]) #加上dp[i]是因为可能不拆了就是最大值
        return dp[n]
