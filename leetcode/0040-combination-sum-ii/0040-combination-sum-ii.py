class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        candidates.sort()

        def backtracking(index,path,current_sum):
            #basecase
            if current_sum==target:
                ans.append(list(path))
                return 
            
            if current_sum>target:
                return
            
            for i in range(index,len(candidates)):
                if i>index and candidates[i]==candidates[i-1]:
                    continue
                path.append(candidates[i])
                backtracking(i+1,path,current_sum+candidates[i])
                path.pop()
        backtracking(0,[],0)
        return ans
        