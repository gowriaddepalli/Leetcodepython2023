# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """

        self.root = root
        self.val = val
        # self.output = []

        output = self.searchBSTHelper(self.root, self.val)
        return output


    def searchBSTHelper(self, root, val):

        if not root:
            return root

        if val == root.val:
            #print(root.val)
            return root
        
        if val > root.val:
            return self.searchBSTHelper(root.right, val)

        if val < root.val:
            return self.searchBSTHelper(root.left, val)
