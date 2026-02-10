class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Base case: x^0 = 1
        if n == 0:
            return 1.0
        
        # Handle negative exponents
        if n < 0:
            x = 1 / x
            n = -n
        
        # Recursive step
        half = self.myPow(x, n // 2)
        
        # If n is even, return half * half
        # If n is odd, return half * half * x
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x

        