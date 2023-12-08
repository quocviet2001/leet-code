#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        nums.append(0)
        result, count = 0, 0
        for i in nums:
            if i: 
                count += 1
            else:
                result = max(count, result)
                count = 0
        return result
# @lc code=end

