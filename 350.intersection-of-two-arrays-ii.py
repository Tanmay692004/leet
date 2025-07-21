#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        for i in nums2:
            if i in nums1:
                res.append(i)
                nums1.remove(i)
        return res
# @lc code=end

