#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sys.set_int_max_str_digits(10000)
        n=int(num1)
        n1=int(num2)
        n2=n+n1
        return str(n2)
# @lc code=end

