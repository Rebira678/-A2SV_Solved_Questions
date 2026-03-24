from collections import Counter
n , m = [int(x) for x in input().split()]
arr1 = Counter([int(x) for x in input().split()])
arr2 = [int(x) for x in input().split()]

c = 0

for i in arr2:
    c += arr1[i]
print(c)

        
