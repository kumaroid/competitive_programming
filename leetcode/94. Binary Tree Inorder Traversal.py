# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):

        def helper(root,result):
          if root != None:
            helper(root.left,result)
            result.append(root.val)
            helper(root.right,result)  

        result = []
        helper(root,result)
        return result
