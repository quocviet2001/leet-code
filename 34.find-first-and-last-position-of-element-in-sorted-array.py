#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = -1
        end = -1
        check = 0
        for i in range(len(nums)):
            if nums[i] == target:
                start = i
                check += 1
                break
        if check == 1:
            end = start
            for j in range(start+1, len(nums)):
                if nums[j] == target:
                    end = j
        return [start, end]
                


# @lc code=end

