# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        que = []
        if root:
            que.append(root)
        while que:
            size = len(que)
            tmp = []
            for _ in range(size):
                node = que.pop(0)
                tmp.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            result.append(tmp)
        result.reverse() #反转列表
        return result
