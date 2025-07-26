#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right= len(numbers) -1
        while right > left:
            sumthing = numbers[left]+ numbers [ right]
            if sumthing == target:
                return [left+1, right+1]
            elif sumthing <target:
                left+=1
            else:
                right-=1
        return []
# @lc code=end

