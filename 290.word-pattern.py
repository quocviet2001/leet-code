#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()

        if len(s) != len(pattern):
            return False
        
        dic = {}

        for i in range(len(s)):
            if (pattern[i] in dic and dic[pattern[i]] != s[i]):
                return False
            elif pattern[i] not in dic and s[i] in dic.values():
                return False
            
            dic[pattern[i]] = s[i]
            
        return True
# @lc code=end

