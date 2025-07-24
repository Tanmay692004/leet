#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest= 0
        l= 0
        counter: dict[str: int]= defaultdict(int)
        for r in range(len(s)):
            counter[s[r]]+=1
            while counter[s[r]]>1:
                counter[s[l]]-=1
            longest = max(longest, r-l+1)
        return longest
# @lc code=end

