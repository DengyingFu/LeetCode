class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        target = sum(nums)//2  
        dp = [0]*(target+1) #12个元素,重量=价值nums[i]
        for i in range(len(nums)):
            for j in range(target, nums[i]-1, -1): #背包容量如果小于i所需容量就无意义
                dp[j] = max(dp[j], dp[j-nums[i]]+nums[i])
            if dp[target]==target:
                return True
        return False
