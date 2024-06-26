#小饼干先分配给胃口小的
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort() #从小到大排序
        s.sort()
        i = 0
        j = 0
        cnt = 0
        while i<len(s) and j<len(g):
            if s[i]>=g[j]:
                cnt+=1
                i+=1
                j+=1
            else:
                i+=1
        return cnt
