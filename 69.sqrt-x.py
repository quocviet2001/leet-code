#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        
        bot = 0
        top = x
        result = 0

        while bot <= top:
            mid = bot + ((top - bot) // 2)
            if mid**2 > x:
                top = mid - 1
            elif mid**2 < x:
                bot = mid + 1
                result = mid
            else: 
                return mid
        
        return result
# @lc code=end

