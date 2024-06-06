# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        que = []   #队列实现层序遍历
        if root:
            que.append(root)  
        while que:  #队列不为空
            size = len(que) #记录每一层的大小
            tmp = []
            for _ in range(size): #pop完这一层的节点
                node = que.pop(0)
                tmp.append(node.val) 
                if node.left:   #把孩子加进队列
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            result.append(tmp)
        return result
