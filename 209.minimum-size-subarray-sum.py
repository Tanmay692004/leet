#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        res = float('inf')
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res= min(r- left +1, res)
                total-=nums[left]
                left+=1
        return 0 if res== float("inf") else res

        
# @lc code=end

