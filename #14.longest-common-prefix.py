#14. Longest Common Prefix
#https://leetcode.com/problems/longest-common-prefix/
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:  
        word=strs[0]  
        ans=[]
        for i in strs:
            if len(i)<len(word):
                word=i
        for i in range(len(word)):
            for j in range(len(strs)):
                if word[i]!=strs[j][i]:
                    return "".join(ans)
            ans.append(word[i])
        return "".join(ans)
