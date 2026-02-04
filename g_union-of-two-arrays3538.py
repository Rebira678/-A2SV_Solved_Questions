#https://www.geeksforgeeks.org/problems/union-of-two-arrays3538/1
class Solution:    
    def findUnion(self, a, b):
        # code here
        a.extend(b)
        return set(a)
