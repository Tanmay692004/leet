#
# @lc app=leetcode id=682 lang=python3
#
# [682] Baseball Game
#

# @lc code=start
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack= []
        for i in range(len(operations)):
            if operations[i]=="C":
                stack.pop()
            elif operations[i]=="D":
                stack.append(2*stack[-1])
            elif operations[i]== "+":
                if len(stack)==1:
                    stack.append(stack[-1])
                else:
                    stack.append(stack[-1]+ stack[-2])
            else:
                stack.append(int(operations[i]))
        return sum(stack)

# @lc code=end

