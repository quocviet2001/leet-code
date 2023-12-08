#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0: return []
        if len(nums) == 1: return [f'{nums[0]}']
        s = []
        pre = start = nums[0]
        for i in nums[1:]:
            if i - pre != 1:
                s.append(f'{start}->{pre}' if pre - start > 0 else f'{pre}')
                start = i
            pre = i
        s.append(f'{start}->{pre}' if pre - start > 0 else f'{pre}')
        return s
# @lc code=end

