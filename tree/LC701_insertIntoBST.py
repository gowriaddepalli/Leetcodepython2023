# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        self.root = root
        self.val = val

        return self.insertBSTHelper(self.root, self.val)


    def insertBSTHelper(self, root, val):

        if not root:
            return TreeNode(val)
        

        if val > root.val:
            root.right = self.insertBSTHelper(root.right, val)
        else:
            root.left = self.insertBSTHelper(root.left, val)
        return root
