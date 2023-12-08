#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        while True:
            if i**2 > num:
                break
            if i**2 == num:
                return True
            i += 1

        return False
# @lc code=end

