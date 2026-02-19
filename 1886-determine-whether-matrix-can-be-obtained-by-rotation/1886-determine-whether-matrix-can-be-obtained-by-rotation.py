class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        def rotate90(m):
            n = len(m)
            # transpose
            for i in range(n):
                for j in range(i+1, n):
                    m[i][j], m[j][i] = m[j][i], m[i][j]
            # reverse rows
            for row in m:
                row.reverse()
        
        for _ in range(4):
            if mat == target:
                return True
            rotate90(mat)
        
        return False
