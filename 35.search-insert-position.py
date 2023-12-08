#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[len(nums)-1]:
            return len(nums)
        elif target < nums[0]:
            return 0
        for i in range(len(nums)):
            if target == nums[i]:
                return i
            if i == len(nums) - 1:
                break
            elif target > nums[i] and target <= nums[i+1]:
                return i + 1
        return 0

# @lc code=end

