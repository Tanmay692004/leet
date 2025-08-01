#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] *len(temperatures)
        stack = []
        for i , t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackind = stack.pop()
                res[stackind] = i- stackind
            stack.append([t,i])
        return res
# @lc code=end

