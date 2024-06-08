"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        que = collections.deque()
        if root:
            que.append(root)
        while que:
            size = len(que)
            for i in range(size, 0, -1):
                node = que.popleft()
                if i==1:  #每层最后一个节点指向None
                    node.next = None
                else:
                    node.next = que[0]
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        return root
