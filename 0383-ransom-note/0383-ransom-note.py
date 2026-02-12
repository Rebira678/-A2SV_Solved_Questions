class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomnote_count=Counter(ransomNote)
        magazine_count=Counter(magazine)

        count=0
        for i in ransomnote_count:
            if ransomnote_count[i]<=magazine_count[i]:
                count+=1
        
        return count==len(ransomnote_count)