class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sorted_str = sorted(strs, key=len)
        checker = sorted_str[0]
        counter = ""

        for idx in range(len(checker)):
            ch = checker[idx]
            count = 0
            for j in range(1, len(sorted_str)):
                if sorted_str[j][idx] == ch:
                    count += 1
                else:
                    return counter
            if count == len(sorted_str) - 1:
                counter += ch
        
        return counter






