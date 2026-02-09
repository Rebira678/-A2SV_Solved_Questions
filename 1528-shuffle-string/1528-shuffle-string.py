class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans=[0]*len(s)
        dic={}
        for i in range(len(s)):
            dic[i]=indices[i]
        for item in dic.items():
            ans[item[1]]=s[item[0]]
        return "".join(ans)
        
        