class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        pre = float('-inf')
        result = 0
        for i in prices:
            if i>=pre:
                pre = i
                stack.append(i)
            else:
                if len(stack)>1:
                    begin = stack.pop(0)
                    last = stack.pop(-1)
                    result += (last-begin)
                    stack.clear()
                    stack.append(i)
                    pre = i
                else:
                    stack.clear()
                    stack.append(i)
                    pre = i
        if stack:
            if len(stack)>1:
                begin = stack.pop(0)
                last = stack.pop(-1)
                result += (last-begin)
        return result
