#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = len(strs[0])
        for i in range(len(strs)):
            if len(strs[i]) < length:
                length = len(strs[i])

        result = ""
        index = 0
        check = True
        while index < length:
            temp = strs[0][index]
            for i in range(len(strs)):
                if temp != strs[i][index]:
                    check = False
            if check:
                result += temp
                index += 1
            else:
                break

        return result

# @lc code=end

