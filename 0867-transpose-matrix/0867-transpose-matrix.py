class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        #the length of rows and coloumns
        rows= len(matrix)
        coloumns= len(matrix[0])

        #initialize the transponse matrix
        transponse = [[0] * rows for _ in range(coloumns)]

        #iterate through the matrix and exchange 
        for i in range(rows):
            for j in range(coloumns):
                transponse[j][i]=matrix[i][j]
        
        return transponse

