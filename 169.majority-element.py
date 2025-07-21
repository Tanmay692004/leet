#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maindict= Counter(nums)
        for i in maindict:
            if maindict[i]> (len(nums)//2):
                return i
                
        
# @lc code=end

