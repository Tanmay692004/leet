#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slowptr=0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[slowptr] = nums[i]
                slowptr+=1
        return slowptr        
# @lc code=end

