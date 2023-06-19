# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        self.root = root
        self.mp = dict()
        self.hd = 0
        self.row = 0
        result = []
        

        self.verticalTraversalHelper(self.root, self.mp, self.row, self.hd)

        self.od = OrderedDict(sorted(self.mp.items()))
        
        print(self.mp)
        print(self.od)

        for dist, row_node in self.od.items():
            result.append(node[1] for node in sorted(row_node, key = lambda node: node[0]))
        
        print(result)

        return result




    def verticalTraversalHelper(self, root, mp, row, hd):
        
        #print(root.val)

        if not root:
            return root

        if not mp.get(hd):
            mp[hd] = [(row, root.val)]
        else:
            mp[hd].append((row, root.val))

        
        
        if root.left:
            #print("left")
            #print(root.left.val)
            self.verticalTraversalHelper(root.left, mp, row+1, hd-1)
        
        if root.right:
            #print("right")
            #print(root.right.val)
            self.verticalTraversalHelper(root.right, mp, row+1, hd+1)
