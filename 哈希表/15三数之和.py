#=========先排序，再双指针，注意去重=======这题用双指针比哈希表简单
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                return res
            if i>0 and nums[i]==nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            while right>left:
                tmp = nums[i]+nums[right]+nums[left]
                if tmp>0:
                    right -= 1
                elif tmp<0:
                    left += 1
                else:
                    res.append([nums[i],nums[left],nums[right]])
                    while right>left and nums[right]==nums[right-1]:
                        right -= 1
                    while right>left and nums[left]==nums[left+1]:
                        left += 1
                    right -= 1
                    left += 1
        return res
