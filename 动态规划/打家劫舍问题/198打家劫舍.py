class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
              
        dp = [0]*(len(nums)) #dp[i]表示从前i（包含i）个房间偷的最大值
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
     
        for i in range(2, len(dp)): 
            dp[i] = max(dp[i-1], dp[i-2]+nums[i]) #不偷i和偷i的两种情况，取最大值
        return dp[-1]
