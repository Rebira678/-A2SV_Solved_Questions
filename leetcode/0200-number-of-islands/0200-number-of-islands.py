class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols=len(grid),len(grid[0])
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        island=0

        def isbound(row,col):
            return 0<=row<rows and 0<=col<cols
     
        def dfs(row,col):
            grid[row][col]='0'

            for row_changed, col_changed in directions:
                new_row,new_col= row + row_changed ,col + col_changed
                if isbound(new_row,new_col) and grid[new_row][new_col]=="1":
                    dfs(new_row,new_col)



        for row in range(rows):
            for col in range(cols):
                if grid[row][col]=='1':
                    island+=1
                    dfs(row,col)
        
        return island
