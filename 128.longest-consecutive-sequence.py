#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums = set(nums)
        for i in nums:
            if i-1 not in nums:
                count=0
                while i+count in nums:
                    count+=1
                longest= max(longest, count)
        return longest
        
# @lc code=end

