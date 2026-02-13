from typing import List

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        if not img:
            return []

        rows, cols = len(img), len(img[0])
        # Prepare a new matrix for the result
        result = [[0 for _ in range(cols)] for _ in range(rows)]
        
        # Directions for neighbors (8 directions + self)
        directions = [(-1,-1), (-1,0), (-1,1),
                      (0,-1),  (0,0),  (0,1),
                      (1,-1),  (1,0),  (1,1)]
        
        for i in range(rows):
            for j in range(cols):
                total, count = 0, 0
                for dr, dc in directions:
                    r, c = i + dr, j + dc
                    if 0 <= r < rows and 0 <= c < cols:
                        total += img[r][c]
                        count += 1
                result[i][j] = total // count  
        return result
