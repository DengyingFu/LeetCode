# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        que = []
        if root:
            que.append(root)
        while que:  #每次pop后把它的右孩子加进队列
            size = len(que)
            for i in range(size, 0, -1):
                node = que.pop(0)
                if i==1:  #每一层最后一个pop的才是最右侧的节点
                    result.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            
        return result
