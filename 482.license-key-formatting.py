#
# @lc app=leetcode id=482 lang=python3
#
# [482] License Key Formatting
#

# @lc code=start
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()
        new_key , dup = '' , k

        for i in range(len(s)-1,-1,-1):
            if k!=0:
                new_key = s[i] + new_key
                k -= 1

            if k == 0 and i != 0:
                new_key = '-' + new_key
                k = dup

        return new_key
# @lc code=end

