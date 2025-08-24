#
# @lc app=leetcode id=1493 lang=python3
#
# [1493] Longest Subarray of 1's After Deleting One Element
#

# @lc code=start
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        start = 0
        length = 0
        zero = -1
        for i in range(len(nums)):
            if nums[i]==0:
                start = zero +1
                zero = i
            length = max(length, i - start)
        return length
# @lc code=end

