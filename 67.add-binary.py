#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        book = 0
        a = a[::-1]
        b = b[::-1]

        leng = max(len(a), len(b))
        for i in range(leng):
            element_A = ord(a[i]) - ord("0") if i < len(a) else 0
            element_B = ord(b[i]) - ord("0") if i < len(b) else 0
            
            sum = element_A + element_B + book
            chr = str(sum % 2)
            result = chr + result
            book = sum // 2

        if book == 1:
            result = "1" + result
        
        return result
            
# @lc code=end

