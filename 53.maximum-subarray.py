#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        sum = 0

        for n in nums:
            if sum < 0:
                sum = 0
            sum += n
            max_sum = max(max_sum, sum)
        return max_sum
# @lc code=end

