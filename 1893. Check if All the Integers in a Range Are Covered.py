#https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/
#1893. Check if All the Integers in a Range Are Covered
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        contain=[]
        for i in range(left,right+1):
            for j in range(len(ranges)):
                if ranges[j][0]<= i <= ranges[j][1]:
                    contain.append(1)
                    break
        return right-left+1==len(contain)
