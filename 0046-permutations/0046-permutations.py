class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtracking(path,used):

            #basecase
            if len(path)==len(nums):
                ans.append(path[:])
                return 
            for i in range(len(nums)):
                if i in used:
                    continue
                path.append(nums[i])
                used.add(i)
                backtracking(path,used)
                path.pop()
                used.remove(i)

        backtracking([], set())
        return ans




















