class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result=[]
        n=[i for i in range(1,n+1)]

        def backtracking(index,path):

            #base_case
            if len(path)==k:
                result.append(path[:])
                return

            if index==len(n):
                return 

            path.append(n[index])
            backtracking(index+1,path)
            path.pop()

            backtracking(index+1,path)
        backtracking(0,[])
        return result