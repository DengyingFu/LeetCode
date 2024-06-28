#五步法
class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        dp = [1]*(n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
#状态压缩，因为dp[n]只依赖于前两个数
class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        dp = [0,1]
        summ = 1
        for i in range(2, n+1):
            summ = dp[0]+dp[1]
            dp[0] = dp[1]
            dp[1] = summ
        return summ
