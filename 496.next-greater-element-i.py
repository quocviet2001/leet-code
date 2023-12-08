#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for num1 in nums1:
            idx = nums2.index(num1)
            check = False
            for j in range(idx+1, len(nums2)):
                if nums2[j] > num1:
                    result.append(nums2[j])
                    check = True
                    break
            if not check:
                result.append(-1)
        return result
# @lc code=end

