#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx  = 0
        while True:
            if idx == len(nums):
                break
            i = idx + 1
            while True:
                if i == len(nums):
                    break
                if nums[idx] == nums[i]:
                    nums.remove(nums[i])
                else:
                    i += 1    
            idx += 1
        return len(nums)
# @lc code=end

