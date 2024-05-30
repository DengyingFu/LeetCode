#=========KMP算法==================
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        nxt = [0]*len(s)
        nxt = self.getnext(nxt, s)
        if (nxt[-1]!=0 and len(s)%(len(s)-nxt[-1])==0):  #最大相同前后缀不包含的字符就是最小组成字符串，如果能被最小组成字符串长度整除就是True
            return True
        return False

    def getnext(self, nxt:list, st:str): #构建next数组，不-1,例如aba对应的nxt是[0,0,1]
        j = 0
        for i in range(1, len(st)):
            while j!=0 and st[i]!=st[j]:
                j = nxt[j-1]
            if st[i]==st[j]:
                j+=1
            nxt[i] = j
        return nxt
