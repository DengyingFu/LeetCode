class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        ans = 0  #统计次数
        cnt = {}  
        #构建哈希表 两层循环O(n2)
        for i in nums1:
            for j in nums2:
                tmp = i+j
                cnt[tmp] = cnt.get(tmp,0) + 1

      #c查找哈希表 两层循环O(n2)
        for k in nums3:
            for l in nums4:
                tmp = -k-l
                if tmp in cnt: #对字典，检查的是键
                    ans += cnt[tmp]  #因为cnt[tmp]是i+j出现的次数，因此一个-k-l对应cnt[tmp]个
        return ans
      #总时间复杂度O(n2)+O(n2) = O(n2)
      #若使用暴力法，直接套四层for循环会超时O(n4)
