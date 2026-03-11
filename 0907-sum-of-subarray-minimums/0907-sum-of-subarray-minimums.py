class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack=[]
        ans=0
        modulo=10**9 + 7
        n=len(arr)


        for i in range(n+1):
            while stack and (i==n or arr[stack[-1]]>arr[i]):
                mid=stack.pop()

                left=mid-(stack[-1] if stack else -1)
                right=i-mid

                ans+=arr[mid]*left*right
            stack.append(i)
        
        return ans % modulo


        








                
