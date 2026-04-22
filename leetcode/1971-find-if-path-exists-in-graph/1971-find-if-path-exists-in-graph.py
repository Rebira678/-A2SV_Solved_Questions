class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph=defaultdict(list)

        for u , v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited=set()
        def dfs (vertex,visited):
            #basecase
            if vertex==destination:
                return True
            
            visited.add(vertex)
            for i in graph[vertex]:
                if i not in visited:
                    if dfs(i,visited):
                        return True
            
            return False
                    
        return dfs(source,visited)
        
