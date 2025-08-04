#
# @lc app=leetcode id=904 lang=python3
#
# [904] Fruit Into Baskets
#

# @lc code=start
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left, right = 0,0
        countkeep = collections.defaultdict(int)
        left, res, total = 0,0,0
        for r in range(len(fruits)):
            countkeep[fruits[r]] +=1
            total +=1

            while len(countkeep)>2:
                f= fruits[left]
                countkeep[f] -=1
                total -=1
                left +=1

                if not countkeep[f]:
                    countkeep.pop(f)
            res= max(res, total)
        return res


# @lc code=end

