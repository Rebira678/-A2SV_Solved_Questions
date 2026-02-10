class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        ans=0
        for i in nums:
            if i-1 not in nums:
                current=i
                leng=1

                while current+1 in nums:
                    current+=1
                    leng+=1

                ans=max(ans,leng)

        return ans
                
            

        