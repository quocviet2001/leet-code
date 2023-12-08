#
# @lc app=leetcode id=504 lang=python3
#
# [504] Base 7
#

# @lc code=start
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        sign = ''
        result = ''
        if num < 0:
            num = -num
            sign = '-'
        while num > 0:
            result += str(num%7)
            num = num //7

        return sign + result[::-1]
# @lc code=end

