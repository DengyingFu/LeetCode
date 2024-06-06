# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.traversal(root, result)
        return result

    def traversal(self, rot, res):
        if rot==None:
            return 
        self.traversal(rot.left, res)
        self.traversal(rot.right, res)
        res.append(rot.val)
