#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        list_index = []
        check1 = True
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                list_index.append(i)
                check1 = False
        if check1:
            return -1
        else:
            for index in list_index:
                if index == len(haystack) - 1:
                    if len(needle) == 1:
                        return index
                    else:
                        return -1
                if (index + len(needle)) > len(haystack):
                    return -1
                check2 = True
                j = 1
                for i in range(index + 1, index + len(needle)):
                    if haystack[i] != needle[j]:
                        check2 = False
                        break
                    else:
                        j += 1
                if check2:
                    return index
        return -1             
# @lc code=end

