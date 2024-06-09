# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        result = 0
        que = []
        if root:
            que.append(root)
        while que:
            size = len(que)
            result += 1
            for _ in range(size):
                node = que.pop(0)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                if node.left==None and node.right==None:
                    return result
        return result
