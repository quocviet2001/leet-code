#
# @lc app=leetcode id=326 lang=python3
#
# [326] Power of Three
#

# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        
        if n == 1:
            return True
        
        while n > 1:
            mod = n % 3
            if mod != 0:
                return False
            n = n // 3
        
        return True
# @lc code=end

