class Solution:
    def fib(self, n: int) -> int:
        """
        state=n
        base case=if n==1 return 1 and if n==0 return 0
        recursion relation:self.fib(n-1)+self.fib(n-2)
        """

        if n==1:
            return 1
        
        if n==0:
            return 0
        
        return (self.fib(n-1)+self.fib(n-2))
        