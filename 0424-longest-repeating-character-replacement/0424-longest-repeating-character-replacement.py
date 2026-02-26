class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        left = 0
        max_len = 0
        max_freq = 0

        for right in range(len(s)):
            # Add current character to count
            count[s[right]]+=1
            # Update max frequency in current window
            max_freq = max(max_freq, count[s[right]])

            # Shrink window if replacements needed exceed k
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            # Update max length
            max_len = max(max_len, right - left + 1)

        return max_len   
