#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = 0
        d = {}
        for x in s:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
            if d[x] % 2 == 1:
                count += 1
            else:
                count -= 1
        if count > 1:
            return len(s) - count + 1
        
        return len(s) 
# @lc code=end

