# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []
        que = []
        if root:
            que.append(root)
        while que:
            size = len(que)
            tmp = 0
            for _ in range(size):
                node = que.pop(0)
                tmp += node.val
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            result.append(float(tmp)/size)
        return result
