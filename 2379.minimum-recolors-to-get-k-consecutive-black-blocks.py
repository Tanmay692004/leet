#
# @lc app=leetcode id=2379 lang=python3
#
# [2379] Minimum Recolors to Get K Consecutive Black Blocks
#

# @lc code=start
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res = 0
        for i in range(k):
            if blocks[i]=="B":
                res+=1
        finres = res
        for j in range(k, len(blocks)):
            if blocks[j]=="B":
                res+=1
            if blocks[j-k]=="B":
                res-=1
            if res> finres:
                finres = res
        return 0 if finres>=k else k-finres
        
# @lc code=end

