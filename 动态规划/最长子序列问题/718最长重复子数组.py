class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        dp = [[0]*(len(nums2)+1) for _ in range(len(nums1)+1)]
        #dp[i][j]表示以nums1[i-1]结尾的和nums[j-1]结尾的公共最长子数组长度
        #所以dp[i][0]和dp[0][j]初始化为0即可，最后要遍历到dp[len(nums1)][len(nums2)]
        for i in range(1, len(nums1)+1):
            for j in range(1, len(nums2)+1):
                if nums1[i-1]==nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j]>res: #记录最大值
                    res = dp[i][j]
        return res
