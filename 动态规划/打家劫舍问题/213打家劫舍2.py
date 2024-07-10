class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:      
            return nums[0]
        nums1 = nums[1:]
        nums2 = nums[0:-1]
        return max(self.way(nums1), self.way(nums2))  #头尾不能同时取，那么就不考虑头或者不考虑尾两种情况取最大值
    def way(self, nums):  #该函数和打家劫舍一样
        if len(nums)==1:
            return nums[0]
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(dp)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[-1]
