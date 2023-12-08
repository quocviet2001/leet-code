#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        for i in ransomNote:
            if i not in magazine:
                return False
            else:
                index = magazine.find(i)
                magazine = my_string = magazine[:index] + magazine[index + 1:]
        return True
            
# @lc code=end

