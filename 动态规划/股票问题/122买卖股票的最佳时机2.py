#===========动态规划====================
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0]*2 for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        result = 0
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]-prices[i]) #第i天持有  此时不是-prices[i]，因为要算是之前的利润
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]+prices[i]) #第i天 不 持有
        return dp[-1][1]

#=========用栈================
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        pre = float('-inf')
        result = 0
        for i in prices:
            if i>=pre:
                pre = i
                stack.append(i)
            else:
                if len(stack)>1:
                    begin = stack.pop(0)
                    last = stack.pop(-1)
                    result += (last-begin)
                    stack.clear()
                    stack.append(i)
                    pre = i
                else:
                    stack.clear()
                    stack.append(i)
                    pre = i
        if stack:
            if len(stack)>1:
                begin = stack.pop(0)
                last = stack.pop(-1)
                result += (last-begin)
        return result
  
