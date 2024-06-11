#=====================递归法============================
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root:
            issame = self.treval(root.left, root.right)
            return issame
        else:
            return True
    def treval(self,left,right):
        if left!=None and right==None:
            return False
        elif left==None and right!=None:
            return False
        elif left==None and right==None:
            return True
        elif left.val != right.val:
            return False
        
        outside = self.treval(left.left,right.right)
        inside = self.treval(left.right,right.left)
        issame = outside and inside
        return issame
