class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        place_h=0
        seeker=0

        for _ in range(len(nums)):
            if nums[seeker]!=0:
                nums[place_h],nums[seeker]=nums[seeker],nums[place_h]
                seeker+=1
                place_h+=1
            else:
                seeker+=1
            