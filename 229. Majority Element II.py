#https://leetcode.com/problems/majority-element-ii/
#229. Majority Element II
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        l=len(nums)//3
        ans=[]
        dic=Counter(nums)
        for i in dic:
            if dic[i]>l:
                ans.append(i)
        return ans
