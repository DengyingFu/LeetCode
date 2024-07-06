class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        result = 1   #返回结果
        dp = [1]*len(nums)  #dp[i]代表以nums[i]结尾的最长严格递增子序列
        for i in range(1, len(nums)): 
            for j in range(i):
                if nums[i]>nums[j]: #如果num[i]>nums[j]，那么dp[i]=dp[j]+1。遍历从0到i-1的j，取最大的dp[j]+1
                    dp[i] = max(dp[j]+1, dp[i])
            if dp[i]>result:
                result = dp[i]
        return result
