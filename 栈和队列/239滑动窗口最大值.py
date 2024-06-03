#=======单调队列：对内元素单调递减或递增=================时间复杂的O(n)，如果用暴力法则复杂度为O(n*k)
from collections import deque

class DDdeque:          #单调队列
    def __init__(self):
        self.que = deque()

    def mypop(self,value):
        if self.que and value == self.que[0]:#要pop的值等于队列的第一个元素时，才pop，否则代表已经pop过就不需要pop了
            self.que.popleft()

    def mypush(self, value):
        while self.que and value > self.que[-1]:#要push的值大于最后一个元素时，弹出最后一个元素再push，保证队列是单调递减的
            self.que.pop()
        self.que.append(value)

    def getmax(self):   #因为是单调递减队列，所以最大值就是第一个元素
        return self.que[0]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = DDdeque()
        res = []
        for i in range(k): #先把k个元素加进去
            que.mypush(nums[i])
        res.append(que.getmax()) #取一次最大值

        for i in range(k, len(nums)): #开始滑动
            que.mypop(nums[i-k]) #先pop窗口移出的元素
            que.mypush(nums[i])  #再push新元素
            res.append(que.getmax())  #求当前窗口最大值
        return res
