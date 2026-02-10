class Solution:
    from collections import defaultdict
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic= defaultdict(int)
        for i in nums:
            dic[i]+=1
        ans=[]
        dic=sorted(dic,key=lambda x: dic[x] ,reverse=True)
        for i in dic:
            if len(ans)<k:
                ans.append(i)

        return ans

