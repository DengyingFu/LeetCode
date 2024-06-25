# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root==None:
            return True
        result = self.getHigh(root)
        return True if result!=-1 else False

    def getHigh(self, node):
        if node==None: #遍历到空节点，返回0
            return 0
        
        lefthigh = self.getHigh(node.left)
        righthigh = self.getHigh(node.right)
        if lefthigh==-1 or righthigh==-1:
            return -1

        if abs(lefthigh-righthigh) > 1:
            return -1
        else:
            return 1+max(lefthigh,righthigh) #叶子节点的高度是1+0=1
