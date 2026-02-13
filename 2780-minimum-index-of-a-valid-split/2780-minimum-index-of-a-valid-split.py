class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        counter = Counter(nums)

        # find dominant element 
        max_freq = max(counter.values())
        dominant = 0

        for k, v in counter.items():
            if v == max_freq:
                dominant = k
                break

        n = len(nums)

        # must dominate whole array
        if max_freq * 2 <= n:
            return -1

        left_count = 0

        for i in range(n):
            if nums[i] == dominant:
                left_count += 1

            left_len = i + 1
            right_len = n - i - 1
            right_count = max_freq - left_count

            if left_count * 2 > left_len and right_count * 2 > right_len:
                return i

        return -1


        


        