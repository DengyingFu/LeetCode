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
