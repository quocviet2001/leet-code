#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        set1 = list(set(nums1))
        set2 = list(set(nums2))

        for num in set1:
            if num in set2:
                result.append(num)
        return result
# @lc code=end

