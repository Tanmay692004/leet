#
# @lc app=leetcode id=1679 lang=python3
#
# [1679] Max Number of K-Sum Pairs
#

# @lc code=start
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d= defaultdict(int)
        pairs= 0
        for num in nums:
            if d[k-num] > 0:
                pairs+=1
                d[k-num] -=1
            else:
                d[num]+=1
        return pairs
        
        """res= 0
        left = 0
        right = len(nums) - 1
        while right> left: 
            sumthing = nums[left] + nums[right]          
            if sumthing == k:
                res+=1
            elif sumthing < k:
                left+=1
            else:
                right-=1
        return res"""  
# @lc code=end

