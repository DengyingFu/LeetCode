#========哈希表解法========
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #哈希表
        record = [0 for _ in range(26)]#对应26个小写字母
        for i in s:
            record[ord(i)-ord('a')]+=1 #a对应第0个元素，如果出现一次就加一。ord函数获取字符的ASCII码
        for j in t:
            record[ord(j)-ord('a')]-=1 #出现一次就减1
        for k in range(26):   #如果最后的record全为0，那么s和t是字母异位词
            if record[k]!=0:
                return False
        return True

#=========Counter函数使用==================
class Solution(object):
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        a_count = Counter(s)
        b_count = Counter(t)
        return a_count == b_count
