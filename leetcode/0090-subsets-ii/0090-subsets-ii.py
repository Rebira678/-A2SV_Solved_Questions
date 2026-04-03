class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()

        def backtracking(index,path):
            ans.append(path[:])

            for i in range(index,len(nums)):
                if i > index and nums[i]==nums[i-1]:
                    continue
                path.append(nums[i])
                backtracking(i+1,path)
                path.pop()

        backtracking(0,[])
        return ans

