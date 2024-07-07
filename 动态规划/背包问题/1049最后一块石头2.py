class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        target = sum(stones)//2 #背包目标容量大小，如果装满则相撞后剩余最少
        dp = [0]*(target+1) 
        for i in range(len(stones)):
            for j in range(target, stones[i]-1, -1):
                dp[j] = max(dp[j], dp[j-stones[i]]+stones[i])
        result = (sum(stones)-dp[target]) - dp[target] #尽可能装石头到背包，剩余的减去装的就是结果
        return result
