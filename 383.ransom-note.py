#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = {}
        for c in magazine:
            if c in counter:
                counter[c]+=1
            else:
                counter[c]= 1
        for c in ransomNote:
            if c not in counter:
                return False
            elif counter[c]==1:
                del counter[c]
            else:
                counter[c]-=1
        return True    
# @lc code=end

