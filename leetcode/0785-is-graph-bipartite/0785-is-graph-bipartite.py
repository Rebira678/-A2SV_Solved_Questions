class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [-1 for _ in range(len(graph))]

        def dfs(node):
            for nei in graph[node]:
                if colors[nei] == -1:  # not colored yet
                    colors[nei] = 1 - colors[node]  # alternate color
                    if not dfs(nei):
                        return False
                elif colors[nei] == colors[node]:  # conflict
                    return False
            return True

        result = True
        for node in range(len(graph)):
            if colors[node] == -1:
                colors[node] = 0
                result = result and dfs(node)

        return result
