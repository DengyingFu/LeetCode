#=========数组实现哈希表==============
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        res = [0]*26
        for i in magazine:
            res[ord(i)-ord('a')] += 1
        for j in ransomNote:
            res[ord(j)-ord('a')] -= 1
            if res[ord(j)-ord('a')]<0:
                return False
        return True
#==========字典实现哈希表==============
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        res = {}
        for i in magazine:
            res[i] = res.get(i, 0) + 1 #注意get的用法，get(key,default)如果key存在则返回对应的值，不存在则返回default
        for j in ransomNote:
            if j in res:
                res[j] -= 1
                if res[j]<0:
                    return False
            else:
                return False
        return True
