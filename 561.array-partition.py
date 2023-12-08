#
# @lc app=leetcode id=561 lang=python3
#
# [561] Array Partition
#

# @lc code=start
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        result = 0
        while i < len(nums):
            result += nums[i]
            i += 2
        return result

# @lc code=end

