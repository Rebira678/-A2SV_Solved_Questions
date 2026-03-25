n , k = map(int,input().split())
a = list(map(int,input().split()))

l = 0
total = 0
answer = 0
for r in range(n):
    total += a[r]
    while total >= k:
        answer += n - r
        total -= a[l]
        l += 1
       
print(answer)
