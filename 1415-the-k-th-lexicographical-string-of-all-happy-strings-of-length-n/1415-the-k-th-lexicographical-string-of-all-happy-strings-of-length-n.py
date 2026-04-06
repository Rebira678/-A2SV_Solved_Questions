class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        letter=["a","b","c"]
        ans=[]
        def backtracking(path):
            #basecase
            if len(path)==n:
                ans.append("".join(path))
                return 
        
            for i in letter:
                if path and path[-1]==i:
                    continue
                
                path.append(i)
                backtracking(path)
                path.pop()
        backtracking([])
        return ans[k-1] if len(ans)>=k else ""
                
