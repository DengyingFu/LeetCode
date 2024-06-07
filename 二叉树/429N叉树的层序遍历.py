"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        result = []
        que = collections.deque()
        if root:
            que.append(root)
        while que:
            size = len(que)
            tmp = []
            for _ in range(size):
                node = que.popleft()
                tmp.append(node.val)
                for child in node.children:
                    que.append(child)
            result.append(tmp)
        return result
