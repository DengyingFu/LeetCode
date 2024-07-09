class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1) #组合成j总金额的 最少硬币个数
        dp[0] = 0
        for coin in coins: #遍历物品
            for j in range(coin, amount+1): #遍历背包
                dp[j] = min(dp[j], dp[j-coin]+1)
        return dp[amount] if dp[amount]!=float('inf') else -1 #如果是inf，则代表没有能够组合成这种总金额的组合
