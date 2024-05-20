class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #双指针 快慢指针法
        fast = 0 #快指针获取新数组的元素（应该不等于val的元素）
        slow = 0 #慢指针是新数组写入的位置
        while fast<len(nums):
            if nums[fast]!=val: #fast等于val时，slow被覆盖，且向前走一步
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
