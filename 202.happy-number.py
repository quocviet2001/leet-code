#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        check = False
        res = n
        count = 0
        while count < 100:
            res = str(res)
            result = 0
            for num in res:
                result += int(num)**2
            res = result
            if result == 1:
                check = True
            count += 1
        return  check  
# @lc code=end

