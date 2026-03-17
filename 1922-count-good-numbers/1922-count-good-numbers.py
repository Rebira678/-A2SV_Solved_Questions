class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        def power(num,exp):
            #base
            if exp==0:
                return 1
            
            half = power(num, exp // 2)
            result = (half * half) % MOD

            if exp % 2 == 1:
                result = (result * num) % MOD

            return result
        

        even = (n + 1) // 2
        odd = n // 2

        return (power(5, even) * power(4, odd)) % MOD
        








        
        
        