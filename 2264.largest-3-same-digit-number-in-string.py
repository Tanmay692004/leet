#
# @lc app=leetcode id=2264 lang=python3
#
# [2264] Largest 3-Same-Digit Number in String
#

# @lc code=start
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        maxgood = ""
        for i in range(len(num) -2):
            if num[i]== num[i+1]== num[i+2]:
                triple = num[i: i +3]
                if triple>maxgood:
                    maxgood= triple
        return maxgood
# @lc code=end

