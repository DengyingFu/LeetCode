#===========库函数的使用=================
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()  #去除两端的空白字符（包括空格和换行符）
        s = s[::-1]   #反转字符串
        s = ' '.join(word[::-1] for word in s.split())  #split将s按空白字符划分为一个列表list，join将反转后的word以空格连接成字符串
        return s
  #==========双指针法=======================
  class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()   #按空白符划分为单词列表
        left = 0
        right = len(words) - 1
        while left<right: 
            words[left],words[right] = words[right],words[left]
            left+=1
            right-=1
        return ' '.join(words)
