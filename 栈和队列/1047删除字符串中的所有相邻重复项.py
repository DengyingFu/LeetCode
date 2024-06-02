#=====双指针=======
class Solution:
    def removeDuplicates(self, s: str) -> str:
        if len(s)<2:
            return s
        left = 0
        right = 1
        s = list(s)
        while right<len(s):
            if s[left]==s[right]:
                s.pop(right)
                s.pop(left)
                if left>0:
                    left = left - 1
                    right = right - 1
            else:
                left += 1
                right += 1
        return ''.join(st for st in s)
#=======栈==============
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for t in s:
            if len(stack)==0 or t!=stack[-1]:
                stack.append(t)
            else:
                stack.pop()
        return ''.join(t for t in stack)
