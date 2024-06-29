class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)] #****如何生成二维数组
        dp[0][0] = 1
        for i in range(m): #必须从0开始，因为边边的行和列也要遍历
            for j in range(n):
                if i==0 and j==0:
                    continue
                dp[i][j] = (dp[i-1][j] if i>0 else 0) + (dp[i][j-1] if j>0 else 0)
        return dp[m-1][n-1]
