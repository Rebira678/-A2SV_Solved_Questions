class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_count=defaultdict(int)
        prefix_count[0]=1
        count=0
        current_sum=0
        for i in nums:
            current_sum+=i

            if (current_sum-goal) in prefix_count:
                count+= prefix_count[current_sum - goal]

            prefix_count[current_sum] += 1
        return count

        