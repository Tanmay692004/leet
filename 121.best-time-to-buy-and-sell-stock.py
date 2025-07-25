#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        mini= prices[0]
        for i in range(1, len(prices)):
            mini = min ( prices[i], mini)
            res = max ( res, prices[i]- mini)
        return res
        
# @lc code=end

