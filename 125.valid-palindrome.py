#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        str = ""
        for char in s:
            if char.isalpha():
                str += char
            elif char.isdigit():
                str += char
        str = str.lower() 

        left, right = 0, len(str) - 1
        check = True
        while left <= right:
            if str[left] != str[right]:
                check = False
                break
            left += 1
            right -= 1
        return check
# @lc code=end

