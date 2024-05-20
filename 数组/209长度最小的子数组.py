class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #滑动窗口法 （也属于双指针）
        left = 0   #开始指针
        sumnum = 0  #窗口内的和
        length = float('inf')
        for i in range(len(nums)): #结束指针
            sumnum = nums[i] + sumnum  #窗口内求和
            while sumnum >= target:  #和超过target，就把开始指针右移一次
                if i - left + 1 < length:  #因为求的是最小的长度
                    length = i - left + 1
                sumnum = sumnum - nums[left]
                left += 1
        if left==0:  #开始指针没动过代表所有元素求和都比target小
            return 0
        else:
            return length
