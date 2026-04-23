class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited=[0 for _ in range(numCourses)]

        graph=defaultdict(list)
        for u,v in prerequisites:
            graph[v].append(u)

        
        def dfs(node):
            if visited[node]==1:
                return False
            elif visited[node]==2:
                return True
            
            visited[node]=1
            for nei in graph[node]:
                if not dfs(nei):
                    return False

            visited[node]=2
            return True
        
        for node in range(numCourses):
            if visited[node]==0:
                if not dfs(node):
                    return False
            
        return True