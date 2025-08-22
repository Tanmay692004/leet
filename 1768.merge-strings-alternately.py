#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#

# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i= 0 
        ans = ""
        n1= len(word1)
        n2= len(word2)
        while i < n1 or i<n2:
            if i  < n1:
                ans +=word1[i]
            if i < n2:
                ans+=word2[i]
            i+=1
        return ans
# @lc code=end

