from typing import List

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        count = 0
        limit = nums[-1]  
        
        for i in range(len(nums)-2, -1, -1): 
            if nums[i] <= limit:
                limit = nums[i]
            else:
                parts = (nums[i] + limit - 1) // limit
                count += parts - 1
                limit = nums[i] // parts  
        return count
