#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        while True:
            if idx == len(nums):
                break
            if nums[idx] == val:
                nums.remove(val)
            else:
                idx += 1
        return idx
# @lc code=end

