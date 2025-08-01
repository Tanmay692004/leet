#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        res= 0
        count ={}
        for r  in range(0, len(s)):
            count[s[r]]= 1 + count.get(s[r], 0)
            while (r-l +1) - max(count.values()) > k:
                count[s[l]] -=1
                l+=1
            res= max(res, r-l+1)
        return res
        
# @lc code=end

