# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        que = []
        res = 0
        if root:
            que.append(root)
        while que:
            size = len(que)
            tmp = []
            for _ in range(size):
                node = que.pop(0)
                if node.left:
                    que.append(node.left)
                    res += node.left.val
                if node.right:
                    que.append(node.right)
        return res
