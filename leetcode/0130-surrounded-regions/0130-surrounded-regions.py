class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        direction=[(1,0),(-1,0),(0,1),(0,-1)]
        rows,cols=len(board),len(board[0])

        def isBound(row,col):
            return (0<=row<rows and 0<=col<cols)

        
        def dfs(row,col):
            if not isBound(row,col) or board[row][col]!="O":
                return 
            board[row][col]="S"
            
            for row_change,col_change in direction:
                dfs(row + row_change,col + col_change)
        


        for r in range(rows):
            dfs(r, 0)          # left border
            dfs(r, cols-1)     # right border
        for c in range(cols):
            dfs(0, c)          # top border
            dfs(rows-1, c)     # bottom border
        
    
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"
