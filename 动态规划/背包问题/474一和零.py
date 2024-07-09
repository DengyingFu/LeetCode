class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0]*(n+1) for _ in range(m+1)] #因为有三个维度：物品一个维度（子集元素个数），重量两个维度m n。所以至少二维数组表示
        #dp[m][n]表示装满容量m，n的背包最多能放多少物品
        for s in strs: #遍历物品 字符串
            x = 0
            y = 0
            for c in s: #统计
                if c=='0':
                    x+=1
                else:
                    y+=1
            for i in range(m, x-1, -1):
                for j in range(n, y-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-x][j-y]+1)
        return dp[m][n]
