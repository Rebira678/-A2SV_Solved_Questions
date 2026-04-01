class Solution:
    def splitString(self, s: str) -> bool:
        def backtracking(index, prev):
            if index == len(s):
                return True

            for j in range(index, len(s)):
                val = int(s[index:j+1])
                if val == prev - 1 and backtracking(j+1, val):
                    return True
            return False
    
        for i in range(len(s)-1):
            first_val = int(s[:i+1])
            if backtracking(i+1, first_val):
                return True
        return False
