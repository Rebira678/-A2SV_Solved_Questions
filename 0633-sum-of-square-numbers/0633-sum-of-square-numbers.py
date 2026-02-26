class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        left=0
        right=int(c**0.5)

        while left<=right:
            product=(left*left + right*right)
            if product==c:
                return True
            elif product<c:
                left+=1
            else:
                right-=1
        
        return False

        