#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#

# @lc code=start
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        
        if n == 1:
            return True
        
        while n > 1:
            mod = n % 4
            if mod != 0:
                return False
            n = n // 4
        
        return True
# @lc code=end

