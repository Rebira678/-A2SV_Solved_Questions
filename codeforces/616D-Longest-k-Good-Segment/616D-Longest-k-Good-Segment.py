#https://codeforces.com/problemset/problem/616/D
from collections import Counter

n, k = map(int, input().split())
x = list(map(int, input().split()))

check = Counter()
distinct = 0
left = 0
ans = 0
l = 1
r = 1

for right in range(n):
    if check[x[right]] == 0:
        distinct += 1
    check[x[right]] += 1
    
    while distinct > k:
        check[x[left]] -= 1
        if check[x[left]] == 0:
            distinct -= 1
        left += 1
    
    if right - left + 1 > ans:
        ans = right - left + 1
        l = left + 1  # 1-based indexing
        r = right + 1

print(l, r)