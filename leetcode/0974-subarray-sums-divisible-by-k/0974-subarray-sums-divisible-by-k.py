class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder_count = defaultdict(int)
        remainder_count[0] = 1
        
        prefix = 0
        count = 0
        
        for num in nums:
            prefix += num
            remainder = prefix % k
            
            count += remainder_count[remainder]
            remainder_count[remainder] += 1
        
        return count

