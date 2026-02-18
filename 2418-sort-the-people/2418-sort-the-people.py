class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n=len(heights)

        for i in range(n):
            finder=i-1
            while finder >=0 and heights[finder]<heights[i]:
                heights[i],heights[finder]=heights[finder],heights[i]
                names[i],names[finder]=names[finder],names[i]
                finder-=1
                     
                
        return names