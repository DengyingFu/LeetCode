class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)#这样dp[0]代表空字符串，dp[j]代表长度为j的字符串是否为True
        dp[0] = True
        #排列问题：先背包再物品
        for j in range(1, len(dp)):
            for i in range(j): #截取字符串 i是截取起始位置，截至位置是j
                word = s[i:j] #截取i到j-1的字符 因为索引从0开始，所以最后一个索引为j-1的字符串长度为j
                if word in wordDict and dp[i]==True:
                    dp[j]=True
        return dp[-1]
