#
# @lc app=leetcode id=507 lang=python3
#
# [507] Perfect Number
#

# @lc code=start
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num < 2:
            return False
        sum = 1
        wish = 2
        limit = int(num ** 0.5) + 1
        while wish < limit:
            if num % wish == 0:
                sum += wish
                if (num//wish) > wish:
                    sum += num // wish
            wish += 1
        
        return sum == num 
# @lc code=end

