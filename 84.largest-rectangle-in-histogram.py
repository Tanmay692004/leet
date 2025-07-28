#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        temp_large= len(heights) * min(heights)
        stack = []
        for i in range(len(heights)):
            if not stack:
                stack.append(heights[i])
            else:
                stack.append(heights[i])
                temp_large = max( temp_large, stack[-2] , heights[i], (min(stack[-2], heights[i]))*2  )
        return temp_large
# @lc code=end

