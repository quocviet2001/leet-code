#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        left = 0
        result = 0

        for right in range(len(s)):
            if s[right] not in dic:
                result = max(result, right - left + 1)
            
            else:
                if dic[s[right]] < left:
                    result = max(result, right - left + 1)
                else:
                    left = dic[s[right]] + 1
                     
            dic[s[right]] = right

        return result
# @lc code=end

