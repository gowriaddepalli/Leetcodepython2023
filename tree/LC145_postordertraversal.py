class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        self.root = root
        self.output = []
        self.postorderTraversal_helper(self.root)
        return self.output

    def postorderTraversal_helper(self, root):
        if not root:
            return
        
        self.postorderTraversal_helper(root.left)
        self.postorderTraversal_helper(root.right)
        self.output.append(root.val)
