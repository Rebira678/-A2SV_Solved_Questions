class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_n=0
        ans=[]
        for i in nums:
            if i%2==0:
                even_n+=i
        
        for i in queries:
            index=i[1]
            value=i[0]
            if nums[index]%2==0:
                even_n-=nums[index]
            nums[index]+=value

            if nums[index]%2==0:
                even_n+=nums[index]
            
            ans.append(even_n)
        return ans