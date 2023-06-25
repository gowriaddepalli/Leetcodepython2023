# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Sea(object):
#    def hasShips(self, topRight, bottomLeft):
#        """
#        :type topRight: Point
#		 :type bottomLeft: Point
#        :rtype bool
#        """
#
# class Point(object):
#	def __init__(self, x, y):
#		self.x = x
#		self.y = y

class Solution(object):
    def countShips(self, sea, topRight, bottomLeft):
        """
        :type sea: Sea
        :type topRight: Point
        :type bottomLeft: Point
        :rtype: integer
        """
        if (topRight.x < bottomLeft.x) or (topRight.y < bottomLeft.y):
            return 0
        
        if not sea.hasShips(topRight, bottomLeft):
            return 0

        if topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
            return 1
        
        midRightX = (topRight.x + bottomLeft.x) // 2
        midRightY = (topRight.y + bottomLeft.y) // 2

        midPoint = Point(midRightX, midRightY)
        midPoint_1 = Point(midRightX+1, midRightY+1)
        
        count = self.countShips(sea, midPoint, bottomLeft) + \
                self.countShips(sea, topRight, midPoint_1) + \
                self.countShips(sea, Point(midRightX, topRight.y), Point(bottomLeft.x, midRightY+1)) + \
                self.countShips(sea, Point(topRight.x, midRightY), Point(midRightX+1, bottomLeft.y)) \

        return count
