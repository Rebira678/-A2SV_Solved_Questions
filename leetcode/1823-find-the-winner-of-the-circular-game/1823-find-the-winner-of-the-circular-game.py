class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        def checker(n):
            if n == 1:
                return 0
            
            return (checker(n - 1) + k) % n
        
        return checker(n) + 1