class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:

        sets=set()
        for i in ranges:
            for j in range(i[0],i[1]+1):
                sets.add(j)
        
        for j in range(left,right+1):
            if j not in sets:
                return False
        
        return True


