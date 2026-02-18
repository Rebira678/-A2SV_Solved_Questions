class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n=len(heights)

        for i in range(n):
            min_index=i
            for j in range(n-1,i,-1):
                if heights[j]>heights[min_index]:
                    heights[min_index],heights[j]=heights[j],heights[min_index]
                    names[min_index],names[j]=names[j],names[min_index]

        
        return names