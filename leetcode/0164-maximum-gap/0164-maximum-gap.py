class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)<2:
            return (0)
        
        nums.sort()
        container=[]
        high=0

        for i in range(1,len(nums)):
            dif=nums[i]-nums[i-1]
            if dif > high:
                high=dif
        
        return high

            