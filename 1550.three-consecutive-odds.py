#
# @lc app=leetcode id=1550 lang=python3
#
# [1550] Three Consecutive Odds
#

# @lc code=start
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        oddcount = 0
        for i in range(len(arr)):
            if arr[i]% 2 == 1:
                oddcount +=1
            else:
                oddcount = 0
            if oddcount == 3:
                return True
        return False
# @lc code=end

