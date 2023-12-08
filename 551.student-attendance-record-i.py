#
# @lc app=leetcode id=551 lang=python3
#
# [551] Student Attendance Record I
#

# @lc code=start
class Solution:
    def checkRecord(self, s: str) -> bool:
    
        a = 0
        l = True
        for i in range(len(s)):
            if s[i] == 'A':
                a += 1
        for i in range(len(s)-1):
            if s[i] == 'L' and i>=1:
                if (len(s) < 3):
                    return True
                if s[i-1] == 'L' and s[i+1] == 'L':
                    l = False
        return a < 2 and l
# @lc code=end

