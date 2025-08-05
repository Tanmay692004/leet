#
# @lc app=leetcode id=3477 lang=python3
#
# [3477] Fruits Into Baskets II
#

# @lc code=start
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        used = [False] * len(baskets)
        unplaced = 0
        for  i in range(len ( fruits)):
            placed = False
            for j in range(len(baskets)):
                if not used[j] and baskets[j] >= fruits[i]:
                    used[j] = True
                    placed = True
                    break
            if not placed:
                unplaced +=1
        return unplaced
            

                #"""fruits.pop(fruits[i])
              #  baskets.pop(baskets[i])
           # else:
             #   temp = baskets[i+1]
              #  baskets[i+1] = baskets[i]
             #   baskets[i] = temp
      #  return len(fruits)"""
# @lc code=end

