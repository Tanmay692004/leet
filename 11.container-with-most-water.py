#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n= len(height)
        l,r = 0, n-1
        res= 0
        while l<r:
            temparea = (((height[l] + height[r]) - abs(height[l] - height[r]))/2) * abs(l - r)
            if height[l] > height[r]:
                r-=1
            else:
                l+=1
            res= max(res, temparea)
        return int(res)
        
# @lc code=end

