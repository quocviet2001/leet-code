#
# @lc app=leetcode id=594 lang=python3
#
# [594] Longest Harmonious Subsequence
#

# @lc code=start
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = Counter(nums)
        max_len = 0

        for key in freq:
            if key + 1 in freq:
                max_len = max(max_len, freq[key] + freq[key+1])
        return max_len
# @lc code=end

