#============用数组做哈希表======================
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [0]*1000
        r = []
        for i in range(len(nums1)):
            result[nums1[i]]=1
        for j in range(len(nums2)):
            if result[nums2[j]]==1:
                result[nums2[j]]=2
        for k in range(1000):
            if result[k]==2:
                r.append(k)
        return r
#===========用字典和集合=================
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 使用哈希表存储一个数组中的所有元素
        table = {}
        for num in nums1:
            table[num] = table.get(num, 0) + 1
        
        # 使用集合存储结果
        res = set()
        for num in nums2:
            if num in table:
                res.add(num)
                del table[num]
        
        return list(res)
