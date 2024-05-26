#=====因为要获取索引，因此选择字典来实现哈希表======
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {} 
        for i in range(len(nums)):
            v = target - nums[i]
            if v in res:
                return [res[v],i]
            else:
                res[nums[i]] = i 
