#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maxPro = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                temp = prices[right] - prices[left]
                maxPro = max(maxPro, temp)
            else:
                left = right
            right += 1
            
        return maxPro

# @lc code=end

