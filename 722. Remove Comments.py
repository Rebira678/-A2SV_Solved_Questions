#https://leetcode.com/problems/remove-comments/description/
#722. Remove Comments
class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        #remove comments for both block comments(/*   */) and the line comments (//)
        check = False
        ans = []
        for j in source:
            i = 0
            if not check:
                new_j = ""
            while i < len(j):
                if not check and i + 1 < len(j) and j[i] == '/' and j[i + 1] == '/':
                    break
                elif not check and i + 1 < len(j) and j[i] == '/' and j[i + 1] == '*':
                    check = True
                    i += 1
                elif check and i + 1 < len(j) and j[i] == '*' and j[i + 1] == '/':
                    check = False
                    i += 1
                elif not check:
                    new_j += j[i]
                i += 1
            if new_j and not check:
                ans.append(new_j)

        return ans
                    
