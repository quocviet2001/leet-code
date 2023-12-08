#
# @lc app=leetcode id=575 lang=python3
#
# [575] Distribute Candies
#

# @lc code=start
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        seen = {}
        i = 0
        amount_allowed = 0
        while(i<len(candyType) and amount_allowed<len(candyType)//2):
            if seen.get(candyType[i],0)==0:
                amount_allowed+=1
                seen[candyType[i]] = 1
            i+=1
        return amount_allowed
# @lc code=end

