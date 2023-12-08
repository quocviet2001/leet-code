#
# @lc app=leetcode id=500 lang=python3
#
# [500] Keyboard Row
#

# @lc code=start
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        dic = {'q': 0, 'w':0, 'e': 0, 'r' : 0, 't': 0,
                'y':0, 'u':0, 'i':0, 'o':0, 'p':0,
                'a': 1, 's':1, 'd':1, 'f':1, 'g':1,
                'h':1, 'j':1, 'k':1, 'l':1, 'z':2,
                'x':2, 'c':2, 'v':2, 'b':2, 'n':2, 'm':2}

        result = []

        for word in words:
            temp = dic[word[0].lower()]
            check = True
            for i in range(1, len(word)):
                if dic[word[i].lower()] != temp:
                    check = False
            if check:
                result.append(word)
        
        return result
                

# @lc code=end

