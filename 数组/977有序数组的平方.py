class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #双指针法
        #因为原数组的绝对值是两头向中间递减的，因此可以两个指针从两头开始先挑
        #大的平方数放进新数组，新数组从右往左填值
        left = 0
        right = len(nums)-1
        k = right
        result = [0]*len(nums)
        while left<=right: #等于时的数也要放进新数组
            if nums[left]**2 < nums[right]**2:
                result[k] = nums[right]**2
                right -= 1
            else:
                result[k] = nums[left]**2
                left += 1
            k -= 1
            
        return result
