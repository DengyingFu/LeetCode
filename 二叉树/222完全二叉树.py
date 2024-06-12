#========递归法=========自己写的
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        self.cnt = 0
        if root:
            self.travel(root)
        return self.cnt
    
    def travel(self, node):
        if node==None:
            return
        self.cnt += 1
        self.travel(node.left)
        self.travel(node.right)
  #=========代码随想录 递归============
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        return self.getNodesNum(root)
        
    def getNodesNum(self, cur):
        if not cur:
            return 0
        leftNum = self.getNodesNum(cur.left) #左
        rightNum = self.getNodesNum(cur.right) #右
        treeNum = leftNum + rightNum + 1 #中
        return treeNum
