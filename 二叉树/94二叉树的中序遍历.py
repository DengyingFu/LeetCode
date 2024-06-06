# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.traversal(root, result)
        return result

    def traversal(self, rot, res):
        if rot==None:
            return
        self.traversal(rot.left, res)
        res.append(rot.val)
        self.traversal(rot.right, res)
