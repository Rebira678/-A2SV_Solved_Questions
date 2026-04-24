class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows,cols = len(heights), len(heights[0])
        pacific_reachable=set()
        atlantic_reachable=set()

        def dfs(r, c, visited, prev_height):
            # Out of bounds or already visited
            if ((r, c) in visited or 
                r < 0 or c < 0 or r >= rows or c >= cols or 
                heights[r][c] < prev_height):
                return
            
            visited.add((r, c))
            
            # Explore neighbors
            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])
     

        
        # start from pacific border
        for col in range(cols):
            dfs(0,col,pacific_reachable,heights[0][col]) #top row
            dfs(rows-1,col,atlantic_reachable,heights[rows-1][col]) #bottom row
        
        for row in range(rows):
            dfs(row, 0, pacific_reachable, heights[row][0])   # left column
            dfs(row, cols-1, atlantic_reachable, heights[row][cols-1]) # right column
        
        
        # Intersection = cells that can reach both oceans
        result = list(pacific_reachable & atlantic_reachable)
        return result






































        