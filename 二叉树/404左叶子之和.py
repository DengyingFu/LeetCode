# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#层序遍历
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
        
# 递归法
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        if root.left==None and root.right==None: #是叶子节点，也终止。因为是父节点才能判断是不是左节点
            return 0
        leftNum = self.sumOfLeftLeaves(root.left)
        if root.left and root.left.left==None and root.left.right==None:
            leftNum = root.left.val
        rightNum = self.sumOfLeftLeaves(root.right)
        res = leftNum + rightNum
        return res
        
   
