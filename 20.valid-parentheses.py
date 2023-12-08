#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {"(" : ")",
           "[" : "]",
           "{" : "}"}
        my_list = []
        if s[0] == ")" or s[0] == "]" or s[0] == "}":
            return False
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                my_list.append(s[i])
            elif s[i] == ")" or s[i] == "]" or s[i] == "}":
                if len(my_list) == 0:
                        return False
                elif s[i] == dic[my_list[-1]]:
                    my_list.pop()
                else:
                    return False
        return not my_list
# @lc code=end

