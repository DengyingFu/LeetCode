class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0]*(target+1)
        dp[0] = 1 #排列问题
        for j in range(1,target+1): #先遍历背包
            for n in nums: #再遍历物品
                if n<=j:
                    dp[j] += dp[j-n]
        return dp[target]
