#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False     
        s=sorted(s)
        t=sorted(t)
        print(s, t)
        if s==t:
            return True
        return False

# @lc code=end

