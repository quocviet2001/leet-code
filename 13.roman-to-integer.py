#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
    
        dic = {"I" : 1,
           "V" : 5,
           "X" : 10,
           "L" : 50,
           "C" : 100,
           "D" : 500,
           "M" : 1000}
        result = dic[s[len(s) - 1]]
        for i in range(len(s) - 2, -1, -1):
            if dic[s[i]] >= dic[s[i+1]]:
                result += dic[s[i]]
            else:
                result -= dic[s[i]]
        return result
