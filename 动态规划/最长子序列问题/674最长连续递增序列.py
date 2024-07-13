class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums) #表示以nums[i]结尾的最长连续递增序列长度
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                dp[i] = dp[i-1]+1
        return max(dp)
