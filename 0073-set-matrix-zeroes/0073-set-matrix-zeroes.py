class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        container=[]
        for i in matrix:
            index_zeros=[]
            for index , value in enumerate(i):
                if value==0:
                    index_zeros.append(index)
            container.append(index_zeros)
        
        for i in range(len(matrix)):
            if len(container[i])>0:
                for j in range(len(matrix[i])):
                    matrix[i][j]=0
        
        indexs=[]
        for i in container:
            for j in i:
                indexs.append(j)
        
        indexs.sort()

        for i in range(len(matrix)):
            for j in indexs:
                matrix[i][j]=0




        


        

        


        