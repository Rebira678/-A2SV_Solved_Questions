class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total=0
        result=[]
        for i in range(len(nums)):
            total+=nums[i]
            result.append(total)
            
        return result
