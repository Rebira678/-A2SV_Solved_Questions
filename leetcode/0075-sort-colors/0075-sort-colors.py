class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counters=Counter(nums)
        index=0
        for i in range(3):
            for j in range(counters[i]):
                nums[index]=i
                index+=1