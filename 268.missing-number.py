#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        limit = len(nums)+1
        lun = [i for i in range(limit)]
        return sum(lun)-sum(nums)
        
# @lc code=end

