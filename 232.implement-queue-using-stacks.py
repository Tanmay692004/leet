#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start
class MyQueue:

    def __init__(self):
        self.queue = []
        self.stack = []
        
    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if not self.queue:
            while self.stack:
                self.queue.append(self.stack.pop())
        return self.queue.pop()

    def peek(self) -> int:
        if not self.queue:
            while self.stack:
                self.queue.append(self.stack.pop())
        return self.queue[-1]

    def empty(self) -> bool:
        return max(len(self.stack), len(self.queue)) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

