#==============递归实现===========
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.traversal(root, result)
        return result

    def traversal(self, rot, res):
        if rot==None:
            return 
        res.append(rot.val)
        self.traversal(rot.left, res)
        self.traversal(rot.right, res)
