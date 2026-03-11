class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack=[]
        next=float('-inf')

        for i in range(len(nums)-1,-1,-1):

            if nums[i]<next:
                return True
            
            while stack and stack[-1]<nums[i]:
                next=stack.pop()
            
            stack.append(nums[i])
        
        return False