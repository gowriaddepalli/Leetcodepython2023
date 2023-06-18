"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        self.output_list = []
        self.node_traversal(root)
        return self.output_list



    def node_traversal(self, root):
        if not root:
            return
        self.output_list.append(root.val)
        for children in root.children:
            self.node_traversal(children)
