#1. Two Sum
#https://leetcode.com/problems/two-sum/submissions/1913572768/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i in range(len(nums)):
            dic[nums[i]]=i
    
        for index,value in enumerate(nums):
            n=target-value
            if n in dic:
                if index==dic[n]:
                    continue
                else:
                    return [index,dic[n]]
