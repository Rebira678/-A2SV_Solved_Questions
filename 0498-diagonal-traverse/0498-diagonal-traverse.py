class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        dic = defaultdict(list)

        # group by diagonal (row + col)
        for r in range(m):
            for c in range(n):
                dic[r + c].append(mat[r][c])

        ans = []

        for k in sorted(dic.keys()):
            if k % 2 == 0:
                ans.extend(dic[k][::-1])  # reverse
            else:
                ans.extend(dic[k])        # normal

        return ans


                
        