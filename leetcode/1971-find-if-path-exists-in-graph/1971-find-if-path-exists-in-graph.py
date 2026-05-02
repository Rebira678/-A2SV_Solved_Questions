class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph=defaultdict(list)
        for i , j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        q=deque([source])
        visited={source}

        while q:
            current=q.popleft()
            if current==destination:
                return True
            
            for nei in graph[current]:
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)
        
        return False

