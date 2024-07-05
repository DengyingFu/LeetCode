class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cover = 0 #覆盖范围
        i = 0
        if len(nums)==1:
            return True
        while i <= cover:
            cover = max(nums[i]+i, cover)
            if cover>=len(nums)-1:
                return True
            i += 1
        return False
