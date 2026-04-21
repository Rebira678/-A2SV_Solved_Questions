class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def backtrack(r):
            #base case: if we placed queens in all rows succesfully
            if r==n:
                copy=board[:]
                sol=[]

                for c in copy:
                    sol.append("".join(c[:]))
                ans.append(sol)
                return

            #try placing queen in each column of current row
            for c in range(n):
                # Skip if column is attacked by another queen:
                # - placedCol: same column
                # - placedPos: same positive diagonal (r + c)
                # - placedNeg: same negative diagonal (r - c)
                if c in placedCol or r + c in placedPos or r - c in placedNeg:
                    continue  
                
                # Place queen and mark attacked positions
                board[r][c] = "Q"
                placedCol.add(c)
                placedPos.add(r + c)
                placedNeg.add(r - c)

                # Recursively try to place queens in next rows
                backtrack(r + 1)

                # Backtrack: remove queen and unmark attacked positions
                board[r][c] = "."
                placedCol.remove(c)
                placedPos.remove(r + c)
                placedNeg.remove(r - c)

        # Initialize empty chess board
        board = [["."] * n for _ in range(n)]
        
        # Sets to track attacked positions:
        placedCol = set()  
        placedPos = set()  
        placedNeg = set()  
        ans = [] 
        
        # Start backtracking from row 0
        backtrack(0)
        return ans

