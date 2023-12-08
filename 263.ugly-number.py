#
# @lc app=leetcode id=263 lang=python3
#
# [263] Ugly Number
#

# @lc code=start
class Solution:
    def isUgly(self, n: int) -> bool:
        if n<=0:
            return False
        
        for i in [2,3,5]:
            while n%i == 0:
                n=n//i
        
        return n == 1
        

# @lc code=end

