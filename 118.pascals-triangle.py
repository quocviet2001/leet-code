#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        result.append([1])
        for i in range(1, numRows):
            result.append([])
            for j in range(i+1):
                if j == 0 or j == i:
                    result[i].append(1)
                else:
                    temp = result[i-1][j-1] + result[i-1][j]
                    result[i].append(temp)
        return result
# @lc code=end

