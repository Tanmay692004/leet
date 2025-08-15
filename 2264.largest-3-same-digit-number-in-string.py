#
# @lc app=leetcode id=2264 lang=python3
#
# [2264] Largest 3-Same-Digit Number in String
#

# @lc code=start
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for i in range(9,-1,-1):
            ans = str(i)*3
            if ans in num:
                return ans
        return "" 
# @lc code=end

