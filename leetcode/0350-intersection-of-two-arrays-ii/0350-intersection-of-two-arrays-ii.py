class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        nums1=Counter(nums1)
        nums2=Counter(nums2)

        for i in nums1:
            if i in nums2 :
                m=min(nums1[i],nums2[i])
                for _ in range(m):
                    ans.append(i)
        return ans