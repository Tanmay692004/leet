#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        counter = defaultdict(int)
        n= len(s)
        for r in range(n):
            counter[s[r]] +=1
            while counter[s[r]] >1:
                counter[s[l]]-=1
                l+=1
            longest = max(longest, r-l +1)
        return longest
# @lc code=end

