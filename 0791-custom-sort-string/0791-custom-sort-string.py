class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        count = Counter(s)
        ans = ""
        
        # Add characters according to 'order'
        for ch in order:
            if ch in count:
                ans += ch * count[ch]
                del count[ch]
        
        # Add remaining characters
        for ch in count:
            ans += ch * count[ch]
        
        return ans
        
