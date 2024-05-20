#二分查找
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #二分法左闭右闭的写法
        length = len(nums)
        if length==0:
            return -1
        left = 0
        right = length - 1
        while left<=right:   #注意这里二分查找的判断条件 以及下面left和right变化的方式
            mid = (left+right)//2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1
