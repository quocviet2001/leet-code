#
# @lc app=leetcode id=506 lang=python3
#
# [506] Relative Ranks
#

# @lc code=start
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        new_list = sorted(score, reverse=True)
        dic = {}
        result = []
        for i in range(len(new_list)):
            if i == 0:
                dic[new_list[i]] = "Gold Medal"
            elif i == 1:
                dic[new_list[i]] = "Silver Medal"
            elif i == 2:
                dic[new_list[i]] = "Bronze Medal"
            else:
                dic[new_list[i]] = str(i+1)
        
        for s in score:
            result.append(dic[s])
        
        return result
# @lc code=end

