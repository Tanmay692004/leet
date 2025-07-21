#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen= set(nums1)
        res=[]
        for i in nums2:
            if i in seen:
                res.append(i)
                seen.remove(i)
        return res


# @lc code=end

