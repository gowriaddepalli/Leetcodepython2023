"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        self.root = root
        self.output = []
        self.postorderhelper(self.root)
        return self.output


    def postorderhelper(self, root):
        if not root:
            return

        for children in root.children:
            self.postorderhelper(children)
        self.output.append(root.val)
