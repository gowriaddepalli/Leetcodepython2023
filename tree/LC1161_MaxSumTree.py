# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
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

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            sum = 0

            for val in level:
                sum += int(val)

            result.append(sum)
        
        max_value = max(result)
        level_index = result.index(max_value)
        return level_index+1
