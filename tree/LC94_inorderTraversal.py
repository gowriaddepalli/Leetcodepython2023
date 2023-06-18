# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.root = root
        self.output = []
        self.inorderhelper(self.root)
        return self.output

    def inorderhelper(self, root):
        if not root:
            return
        
        self.inorderhelper(root.left)
        self.output.append(root.val)
        self.inorderhelper(root.right)
