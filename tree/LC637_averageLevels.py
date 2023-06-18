# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """

        nodes = deque()                     # Node processing queue
        level = count = 0                   # current level, count so far within this level
        row_avg = [0]                       # Average of node values in each row
        nodes.appendleft(root)
        nodes.appendleft(None)              # Marker for a level change
        while nodes:
            # Proceed through the nodes queue, summing and recording levels to a list
            node = nodes.pop()
            if node:
                # Add node.val to the row total
                count += 1
                row_avg[level] += node.val
                # Replenish the queue
                if node.left:
                    nodes.appendleft(node.left)
                if node.right:
                    nodes.appendleft(node.right)
            else:                           # Done with this level
                row_avg[level] /= float(count)     # Replace sum with average
                if nodes:                   # Non-empty queue; begin next level
                    nodes.appendleft(None)
                    level += 1
                    row_avg.append(0)       # Create new row_avg[level]
                    count = 0
        return row_avg
