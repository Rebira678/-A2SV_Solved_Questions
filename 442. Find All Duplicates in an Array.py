#
#https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        collection=Counter(nums)
        ans=[]
        for i in collection:
            if collection[i]>1:
                ans.append(i)
        return ans
        
