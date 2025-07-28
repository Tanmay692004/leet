#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        

        
        #ok im finally giving up, gotta do this with stack after watching a neetcode video 
        """left = 0
        right = len(heights) -1
        while left < right:
            max_temp = (right - left + 1) *min(heights) 
            if heights[left ] < heights[ right]:
                max_temp = max (max_temp, (min(heights[left: right+1]))*(right-left+1)   )
            else: 
                max_temp = max (max_temp, (min(heights[left: right]))*(right - left +1)  )
            left+=1
            right-=1

        return max(set(heights)) if len(set(heights))==1 else max_temp"""


        """temp_large= len(heights) * min(heights)
        stack = []
        for i in range(len(heights)):
            if not stack:
                stack.append(heights[i])
            else:
                stack.append(heights[i])
                temp_large = max( temp_large, stack[-2] , heights[i], (min(stack[-2], heights[i]))*2,   )
        return temp_large"""
# @lc code=end

