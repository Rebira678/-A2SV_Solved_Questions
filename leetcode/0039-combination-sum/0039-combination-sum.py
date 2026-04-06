class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        def backtracking(index,path,current_sum):
            #basecase
            if current_sum==target:
                ans.append(list(path))
                return 
            if current_sum>target:
                return
            
            for i in range(index,len(candidates)):
                path.append(candidates[i])
                backtracking(i,path,current_sum+candidates[i])
                path.pop()
        
        backtracking(0,[],0)
        return ans
