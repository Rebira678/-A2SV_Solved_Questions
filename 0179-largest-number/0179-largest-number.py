class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        # Convert integers to strings
        nums = list(map(str, nums))
        
        # Custom comparator: sort so that 'ab' > 'ba' for largest number
        def compare(a, b):
            if a + b > b + a:
                return -1  # a should come before b
            elif a + b < b + a:
                return 1   # b should come before a
            else:
                return 0   # equal
        
        # Sort using custom comparator
        nums.sort(key=cmp_to_key(compare))
        
        # Handle case where result is all zeros 
        if nums[0] == '0':
            return '0'
        
    
        return ''.join(nums)   