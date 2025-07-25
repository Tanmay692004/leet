#
# @lc app=leetcode id=3487 lang=python3
#
# [3487] Maximum Unique Subarray Sum After Deletion
#

# @lc code=start
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        res = set()
        l= 0
        r= len(nums) - 1
        for i in range(r+1):
            if len(nums) ==1 or all(x<0 for x in nums):
                return max(nums)
            else:
                if  nums[i]>0:
                    res.add(nums[i])
        return sum(res)
        
# @lc code=end

