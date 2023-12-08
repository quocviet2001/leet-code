#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        set_nums = set()
        left = 0

        for right in range(len(nums)):
            if right - left > k:
                set_nums.remove(nums[left])
                left += 1
            if nums[right] in set_nums:
                return True
            set_nums.add(nums[right])
        return False
# @lc code=end

