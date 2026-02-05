#1160. Find Words That Can Be Formed by Characters
#https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans=[]
        for word in words:
            count=0
            m=0
            for w in word:
                if chars.count(w)>=word.count(w):
                    count+=1
            if count==len(word):
                ans.append(word)
            count=0

        final=0
        for i in ans:
            final+=len(i)
        return final
