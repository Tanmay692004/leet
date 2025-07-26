#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):
        self.MinStack= []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min( val, self.MinStack[-1] if self.MinStack else val)
        self.MinStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.MinStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.MinStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

