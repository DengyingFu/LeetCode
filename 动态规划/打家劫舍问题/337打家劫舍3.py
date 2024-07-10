# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        result = self.r(root)
        return max(result)

    def r(self, tree):#返回dp数组，dp[0]代表不偷该节点时的最大值，dp[1]表示偷该节点时的最大值
        if tree==None:
            return [0,0]
        leftdp = self.r(tree.left)
        rightdp = self.r(tree.right)

        
        val1 = max(leftdp[0], leftdp[1]) + max(rightdp[0], rightdp[1])#不偷该节点，则左右孩子可偷可不偷
        val2 = tree.val + leftdp[0] + rightdp[0] #偷该节点，则不偷左右孩子
        return [val1, val2] #dp[0]代表偷，dp[1]代表不偷，所以不偷的放在第一个
