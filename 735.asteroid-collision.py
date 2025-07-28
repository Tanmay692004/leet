#
# @lc app=leetcode id=735 lang=python3
#
# [735] Asteroid Collision
#

# @lc code=start
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            while stack and i<0 and stack[-1] > 0:
                diff = i+ stack [ -1]
                if diff <0: #nega biga
                    stack.pop()
                elif diff > 0 : 
                    i=0
                else:   #wow, equality
                    i=0
                    stack.pop()
            if i:
                stack.append(i)
        """for i in range(len(asteroids)):
            if not stack: #khali hai
                stack.append(asteroids[i])
            else: #element hai
                if asteroids[i] > 0:
                    stack.append(asteroids[i])
                else: #negative kaleshi
                    if stack[i-1] > 0 and  abs(asteroids[i]) > stack[i-1]: #pichla num +ve dir and nye se chota
                        stack.pop()
                        stack.append(asteroids[i])
                    elif stack[i-1]>0 and abs(asteroids[i]) < stack[i-1]:
                        continue
                    elif stack[i-1] >0 and abs(asteroids[i]) == stack[i-1]:
                        stack.pop()
                    else:
                        stack.append(asteroids[i])"""
        return stack                
                    
        """for  i in range(len(asteroids)):
                if abs(asteroids[i])== asteroids[i]:
                    stack.append(asteroids[i])
                else:
                    if stack[-1]> abs(asteroids[i]):
                        continue
                    elif stack[-1] == abs(asteroids[i]):
                        stack.pop()
                     
                    else: 
                        stack.pop()
        return stack"""       
# @lc code=end

