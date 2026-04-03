import itertools
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        contact= {
            "2": "abc", "3": "def",
            "4": "ghi", "5": "jkl", "6": "mno",
            "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        ans=[]
        def backtracking(index,path):
            #base case
            if len(digits)==index:
                ans.append(path)
                return 

            possible_letter=contact[digits[index]]
            for j in possible_letter:
                backtracking(index+1,path+j)
        
        backtracking(0,"")
        return ans

































































            
    