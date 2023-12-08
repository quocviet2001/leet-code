#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for s in columnTitle:
            d = ord(s) - ord('A') + 1
            result = result * 26 + d
        return result
# @lc code=end

