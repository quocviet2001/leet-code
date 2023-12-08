#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        temp = num
        while True:
            n = str(temp)
            result = 0
            for i in n:
                result += int(i)
            if result // 10 == 0:
                return result
            else:
                temp = result
# @lc code=end

