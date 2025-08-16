#
# @lc app=leetcode id=1323 lang=python3
#
# [1323] Maximum 69 Number
#

# @lc code=start
class Solution:
    def maximum69Number (self, num: int) -> int:
        numlinumli_mere_yaar_di = [int(i) for i in str(num)]
        for i in (range(len(numlinumli_mere_yaar_di))):
            if numlinumli_mere_yaar_di[i]!=9:
                numlinumli_mere_yaar_di[i]=9
                break
        return int("".join(map(str,numlinumli_mere_yaar_di)))
# @lc code=end

