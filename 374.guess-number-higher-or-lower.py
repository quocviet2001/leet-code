#
# @lc app=leetcode id=374 lang=python3
#
# [374] Guess Number Higher or Lower
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        first = 1
        last = n
        while first <= last:
            mid = first + (last - first) // 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                last = mid - 1
            else:
                first = mid + 1
            
        
        
# @lc code=end

