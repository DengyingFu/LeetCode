class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1) #dp[j]表示重量为j的背包最多装的多少。如果dp[m]=m则功耗凑出总金额
        dp[0] = 1 #组合问题dp[0]初始化为1
        for coin in coins:
            for j in range(coin, amount+1):#完全背包，物品可重复用，所以正序遍历容量
                dp[j] += dp[j-coin] #组合问题
        return dp[amount]
