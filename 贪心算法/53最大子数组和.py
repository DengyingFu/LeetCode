class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = float('-inf') #初始化为最小值
        count = 0
        for i in nums:
            count += i 
            if count>result:  
                result = count
            if count<0:  #如果累计和小于0，那么应该重新累积
                count = 0
        return result
