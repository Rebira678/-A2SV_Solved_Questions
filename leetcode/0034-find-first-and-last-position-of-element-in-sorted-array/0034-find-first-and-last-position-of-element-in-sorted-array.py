class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def get_starting_pos(nums,target):
            left=0
            right=len(nums)-1
            ans=-1

            while left<=right:
                mid=(left+right)//2

                if nums[mid]==target:
                    ans=mid
                    right=mid-1
                elif nums[mid]> target:
                    right=mid-1
                else:
                    left=mid+1
            
            return ans
        
        def get_ending_pos(nums,target):
            left=0
            right=len(nums)-1
            ans=-1

            while left<=right:
                mid=(left+right)//2

                if nums[mid]==target:
                    ans=mid
                    left=mid+1
                elif nums[mid]> target:
                    right=mid-1
                else:
                    left=mid+1
            
            return ans
        
        return [get_starting_pos(nums,target),get_ending_pos(nums,target)]
