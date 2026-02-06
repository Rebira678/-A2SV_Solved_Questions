#https://leetcode.com/problems/single-number/description/
#136. Single Number
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans=0
        for num in nums:
            ans=ans^num
        return ans
