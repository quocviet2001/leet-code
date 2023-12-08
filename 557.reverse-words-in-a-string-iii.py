#
# @lc app=leetcode id=557 lang=python3
#
# [557] Reverse Words in a String III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        result = ''
        for i in s:
            result += i[::-1] + ' '
        
        return result.rstrip()
# @lc code=end

