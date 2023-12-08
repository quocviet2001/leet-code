#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        j=0
        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                i+=1
            j+=1

        if i==len(s):
            return True
        else:
            return False
        
# @lc code=end

