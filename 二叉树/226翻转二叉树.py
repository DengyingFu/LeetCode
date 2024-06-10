#============从上到下每一层依次翻转=====
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        que = []
        if root:
            que.append(root)
        while que:
            size = len(que)
            for _ in range(size):
                node = que.pop(0)
                node.left,node.right = node.right,node.left
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        return root
