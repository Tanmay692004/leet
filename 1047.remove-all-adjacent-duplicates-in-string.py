#
# @lc app=leetcode id=1047 lang=python3
#
# [1047] Remove All Adjacent Duplicates In String
#

# @lc code=start
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in s:
            if not stack:
                stack.append(i)
            else:
                if stack[-1]==i:
                    stack.pop()
                else:
                    stack.append(i)
        return "".join(stack)
        
# @lc code=end

