#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = []
        result.append([1])
        for i in range(1, rowIndex+1):
            result.append([])
            for j in range(i+1):
                if j == 0 or j == i:
                    result[i].append(1)
                else:
                    temp = result[i-1][j-1] + result[i-1][j]
                    result[i].append(temp)
        return result[rowIndex]
# @lc code=end

