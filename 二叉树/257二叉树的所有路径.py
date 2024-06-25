#-----------------递归 回溯----------------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root==None:
            return []
        result = []
        path = []
        self.traversal(root, path, result)
        return result

    def traversal(self, node, path, result):
        path.append(node.val)
        if node.left==None and node.right==None:
            s = str()
            for i in range(len(path)-1):
                s += str(path[i])
                s += '->'
            s += str(path[len(path)-1])
            result.append(s)
            return 

        if node.left: #回溯和递归要放在一起
            self.traversal(node.left, path, result)
            path.pop() #因为list是不可变对象，所以每次回溯需要pop。
        if node.right:
            self.traversal(node.right, path, result)
            path.pop()
