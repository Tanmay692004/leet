#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack= []
        mapping = {')': '(', '}': '{', ']': '['}
        for i in s:
            if i in "{[(":
                stack.append(i)
            else:
                if not stack or stack[-1]!= mapping[i]:
                    return False
                stack.pop()
        return not stack
        
# @lc code=end

