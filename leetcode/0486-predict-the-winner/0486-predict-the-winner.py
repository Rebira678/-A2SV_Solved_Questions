class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        def solve(l,r):
            if l==r:
                return nums[l]
            
            pick_left=nums[l]-solve(l+1,r)
            pick_right= nums[r]-solve(l,r-1)

            return max(pick_left,pick_right)
        
        return solve(0,len(nums)-1) >= 0