#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res= [-1] *len(nums1)
        hashmap = {i:nums1.index(i) for i in (nums1)}
        for i in range(len(nums2)):
            if nums2[i] not  in hashmap:
                continue
            for j in range(i+1, len(nums2)):
                if nums2[j]> nums2[i]:
                    ind = hashmap[nums2[i]]
                    res[ind]= nums2[j]
                    break

        return res

        
# @lc code=end

