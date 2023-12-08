#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lis=list(strs)
        res=[]
        dic={}
        for i in range(len(lis)):
            s=list(lis[i])
            s.sort()
            s="".join(s)
            lis[i]=s
        for i in range(len(lis)):
            if lis[i] in dic:
                dic[lis[i]].append(i)
            else:
                dic[lis[i]]=[i]
        for i in dic:
            temp=[]
            for j in dic[i]:
                temp.append(strs[j])
            res.append(temp)
        return res
# @lc code=end

