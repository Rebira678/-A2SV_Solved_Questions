class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left=0
        right=len(citations)-1
        ans=0
        n=len(citations)
        while left <= right:
            mid=(left+right)//2
            k= n-mid
            if citations[mid]>=k:
                ans=k
                right=mid-1
            else:
                left=mid+1
        return ans



