class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dic = {0: -1}  
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            rem = total % k

            if rem in dic:
                if i - dic[rem] > 1:
                    return True
            else:
                dic[rem] = i

        return False