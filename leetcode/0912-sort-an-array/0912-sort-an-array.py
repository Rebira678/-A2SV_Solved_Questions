class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(left_half,right_half):
            ans=[]
            ptr1=0
            ptr2=0
            while ptr1 < len(left_half) and ptr2 < (len(right_half)):
                if left_half[ptr1]<= right_half[ptr2]:
                    ans.append(left_half[ptr1])
                    ptr1+=1
                else:
                    ans.append(right_half[ptr2])
                    ptr2+=1
            ans.extend(left_half[ptr1:])
            ans.extend(right_half[ptr2:])
            return ans

        def merge_sort(left,right,nums):
            if right==left:
                return [nums[left]]

            mid=left + (right-left)//2
            left_half=merge_sort(left,mid,nums)
            right_half=merge_sort(mid+1,right,nums)

            return merge(left_half,right_half)
        

        return merge_sort(0,len(nums)-1,nums)
