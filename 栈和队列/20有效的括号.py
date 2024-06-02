class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {'(':')', '[':']', '{':'}'}
        for t in s:
            if t in dic:
                stack.append(t)
            else:
                if len(stack)!=0:
                    p = stack.pop()
                    if t!=dic[p]:
                        return False
                else:
                    return False
        
        return True if len(stack)==0 else False
