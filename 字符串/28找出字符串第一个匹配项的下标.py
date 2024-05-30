#=========暴力法（自己写的=================
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h_len = len(haystack)
        n_len = len(needle)
        i = 0
        j = 0
        while i<h_len:  #保证不超过边界
            if haystack[i]==needle[j]:  #匹配时ij都加一
                i+=1
                j+=1
            else:                       #不匹配时i回溯，j回到0
                i = i-j+1
                j = 0
            if j==n_len:                #如果j超出索引，则找到全部匹配的了
                return i-j             #返回起始索引
        return -1
#===========KMP算法====================
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h_len = len(haystack)
        n_len = len(needle)
        if n_len == 0:
            return 0
        # 构建 next 数组
        nexts = [0] * n_len
        j = 0
        for i in range(1, n_len):
            while j > 0 and needle[i] != needle[j]:
                j = nexts[j - 1]     #nexts[j]代表第0个到j个字符的相同前后缀，如果第j个字符不匹配，那么要找前j-1个字符的最大相同前后缀，因此是nexts[j-1]
            if needle[i] == needle[j]:
                j += 1
            nexts[i] = j
        # 匹配过程
        j = 0
        for i in range(h_len):
            while j > 0 and haystack[i] != needle[j]:
                j = nexts[j - 1]
            if haystack[i] == needle[j]:
                j += 1
            if j == n_len:
                return i - n_len + 1
        
        return -1
