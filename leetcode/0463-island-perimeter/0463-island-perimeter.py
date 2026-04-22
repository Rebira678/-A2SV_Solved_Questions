class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        direction=[(0,1),(0,-1),(1,0),(-1,0)]
        visited=[[False for _ in range(cols)] for _ in range(rows)]


        def inbound(row,col):
            return (0<=row<rows) and (0<=col<cols)

        def dfs (grid,visited,row,col):
            #basecase
            visited[row][col]=True

            perimeter=0

            for row_change,col_change in direction:
                new_row = row + row_change
                new_col = col + col_change

                if not inbound(new_row,new_col) or grid[new_row][new_col]==0:
                    perimeter+=1
                elif inbound(new_row,new_col) and not visited[new_row][new_col]:
                    perimeter+= dfs(grid,visited,new_row,new_col)

            return perimeter

        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==1:
                    return dfs(grid,visited,row,col)


        return 0
