"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        queue = []
        result = []
        
        if root:
            queue.append(root)

        while queue:
            size = len(queue)
            level = []

            for i in range(size):
                node = queue.pop(0)
                level.append(node.val)
                
                if node: 
                    queue.extend(node.children)

        
            result.append(level)

        return result

