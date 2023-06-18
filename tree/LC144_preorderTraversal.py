# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.output_list = []
        self.root = root
        self.node_traveral(self.root)
        return self.output_list
        



    def node_traveral(self, root):
        if not root:
            return
        self.output_list.append(root.val)
        self.node_traveral(root.left)
        self.node_traveral(root.right)


