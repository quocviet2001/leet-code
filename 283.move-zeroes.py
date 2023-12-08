#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = 0
        
        for num in nums:
            if num != 0:
                nums[idx] = num
                idx += 1
            
        for i in range(idx, len(nums)):
            nums[i] = 0

# @lc code=end

