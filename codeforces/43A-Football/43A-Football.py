from collections import defaultdict
t=int(input())
collections=defaultdict(int)
for _ in range(t):
    string=input()
    collections[string]+=1

collections = sorted(collections.items(), key=lambda x: x[1])

print(collections[-1][0])