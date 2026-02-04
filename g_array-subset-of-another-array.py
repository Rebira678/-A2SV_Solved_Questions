#https://www.geeksforgeeks.org/problems/array-subset-of-another-array2317/1
#User function Template for python3
from collections import Counter
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        a.sort()
        b.sort()
        c_a=Counter(a)
        c_b=Counter(b)
        count=0
        for i in c_b:
            if i in c_a and c_b[i]<=c_a[i]:
                count+=1
            else:
                return False
        return count==len(c_b)
    
