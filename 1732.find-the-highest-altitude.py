#
# @lc app=leetcode id=1732 lang=python3
#
# [1732] Find the Highest Altitude
#

# @lc code=start
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = 0 
        maxalt = 0
        for i in gain:
            alt+=i
            maxalt = max(maxalt, alt)
        return maxalt
# @lc code=end

