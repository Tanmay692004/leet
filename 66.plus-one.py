#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digitsnum = "".join(map(str, digits))
        num = int(digitsnum) + 1
        return list(map(int, str(num)))
# @lc code=end

