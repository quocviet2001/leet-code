#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        
        prev1, prev2 = 0, 1
        
        for _ in range(n-1):
            prev1, prev2 = prev2, prev1 + prev2
        
        return prev2
# @lc code=end

