#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res= []
        nums.sort()
        for i,a in enumerate(nums):
            if i>0 and a== nums[i-1]:
                continue
            l,r  = i+1, len(nums) - 1
            while l<r:
                triplet = a+ nums[l]+ nums[r]
                if triplet == 0:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l<r and nums[l] == nums[l-1]:
                        l += 1
                    while l<r and nums[r] == nums[r+1]:
                        r -= 1
                elif triplet < 0:
                    l += 1
                else:
                    r -= 1
        return res
# @lc code=end

