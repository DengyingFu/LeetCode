#==========暴力法：先统计所有元素频率，然后排序，然后取前k个==============
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_set = set(nums)
        counts = [] #存储数字及其对应的频率
        for i in nums_set:
            counts.append([i,nums.count(i)])
        counts.sort(key=lambda x:x[1],reverse=True)#按频率降序排序
        res = [] #返回结果
        for i in range(k):
            res.append(counts[i][0])
        return res
#===========小顶堆 O(nlogk)===================
import heapq 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map_ = dict()
        for n in nums:
            map_[n] = map_.get(n, 0)+1
        
        pri_heapq = [] #小顶堆
        for key,freq in map_.items(): #注意items方法的使用：items() 方法把字典中每对 key 和 value 组成一个元组，并把这些元组放在列表中返回
            heapq.heappush(pri_heapq, (freq, key)) #按freq建堆，堆元素是元组（也可以是list）
            if len(pri_heapq) > k: #维护k个数值，当堆里元素大于k时，pop堆顶的（即最小的）。所以留在堆里的是k个最大的元素
                heapq.heappop(pri_heapq)

        res = [0]*k
        for i in range(k):
            res[i] = pri_heapq[k-i-1][1]
        return res
