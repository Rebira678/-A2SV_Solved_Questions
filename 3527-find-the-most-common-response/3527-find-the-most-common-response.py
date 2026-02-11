class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        ans=[]
        res = []
        for sub in responses:
            seen = set()
            temp = []
            for word in sub:
                if word not in seen:
                    seen.add(word)
                    temp.append(word)
            res.append(temp)
        
        dic=defaultdict(int)
        for i in res:
            for j in i:
                dic[j]+=1
        
        max_value=max(dic.values())
        for i in dic:
            if dic[i]==max_value:
                ans.append(i)
        ans.sort()
        if ans:
            return ans[0]
        else:
            return ""

        


                