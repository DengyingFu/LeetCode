#================组合问题================
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if(target+sum(nums))%2:
            return 0
        if abs(target)>sum(nums):
            return 0
        A = (target+sum(nums))//2
        dp = [0]*(A+1)
        dp[0] = 1
        for i in range(len(nums)):
            for j in range(A, nums[i]-1, -1):
                dp[j] += dp[j-nums[i]]
        return dp[A]
