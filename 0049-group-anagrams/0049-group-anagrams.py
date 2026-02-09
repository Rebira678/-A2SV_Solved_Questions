class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans={}
        for i in strs:
            m=str(sorted(i))
            if m in ans:
                ans[m].append(i)
            else:
                ans[m]=[i]
        final=[]
        for i in ans:
            final.append(ans[i])
        return final