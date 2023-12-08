#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        sum = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1 
            while l < r:
                temp = nums[i] + nums[l] + nums[r]
                if abs(target - temp) < abs(sum - target):
                    sum = temp
                if temp > target:
                    r -= 1
                else:
                    l += 1
        return sum
            



# @lc code=end

