#============广度优先，层次遍历=====
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
            for _ in range(size): #广度优先，for循环遍历完当前层节点
                node = que.pop(0)
                node.left,node.right = node.right,node.left
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        return root
#==========深度优先，前序遍历，迭代法（模拟递归）====================
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = []
        if root:
            stack.append(root)
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root
#=========深度优先，前序遍历，递归法========
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traveral(node):
            if node==None:
                return
            node.left, node.right = node.right, node.left
            traveral(node.left)
            traveral(node.right)
        traveral(root)
        return root
