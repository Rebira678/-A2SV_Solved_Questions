class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in nums:
            index=abs(i)-1
            if nums[index]<0:
                ans.append(abs(i))
            else:
                nums[index]=-nums[index]
        return ans