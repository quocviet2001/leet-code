#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        unique_elements = list(set(nums))
        majority_element = unique_elements[0]
        max_count = 0
        for element in unique_elements:
            count = nums.count(element)
            if count > max_count:
                max_count = count
                majority_element = element
        return majority_element
# @lc code=end

