#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        nums1=sorted(nums1)
        nums2= sorted(nums2)
        i,j=0,0
        while i< len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                i+=1
            elif nums1[i]> nums2[j]:
                j+=1
            else:
                res.append(nums1[i])
                i+=1
                j+=1
        return res
# @lc code=end

