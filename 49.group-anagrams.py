#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap= defaultdict(list)
        for i in strs:
            count=[0]*26
            for chrs in i:
                count[ord(chrs) - ord("a")] +=1
            hashmap[tuple(count)].append(i)
        return list(hashmap.values())
# @lc code=end

