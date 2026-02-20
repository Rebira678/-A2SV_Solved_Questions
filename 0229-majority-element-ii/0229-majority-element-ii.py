class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        dic=defaultdict(int)

        for i in nums:
            dic[i]+=1
        
        ans=[]
        m=int(n/3)
        for i in dic:
            if dic[i]>m:
                ans.append(i)

        return ans