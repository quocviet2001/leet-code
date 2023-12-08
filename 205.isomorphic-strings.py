#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST = {}
        mapTS = {}

        for char1, char2 in zip(s, t):
            if (char1 in mapST and mapST[char1] != char2) or\
                (char2 in mapTS and mapTS[char2] != char1):
                return False
            mapST[char1] = char2
            mapTS[char2] = char1
        return True
# @lc code=end

