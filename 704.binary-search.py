#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)- 1
        while left <=right:
            midn= (left+right)//2
            if nums[midn] > target:
                right= midn-1
            elif nums[midn] < target:
                left = midn+1
            else:
                return midn
        return -1 
# @lc code=end

