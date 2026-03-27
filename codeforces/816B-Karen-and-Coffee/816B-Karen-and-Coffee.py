n, k, q = map(int, input().split())

recipes = []
max_temp = 0

for _ in range(n):
    l, r = map(int, input().split())
    recipes.append((l, r))
    if r > max_temp:
        max_temp = r

queries = []
for _ in range(q):
    a, b = map(int, input().split())
    queries.append((a, b))
    if b > max_temp:
        max_temp = b

diff = [0] * (max_temp + 3)

for l, r in recipes:
    diff[l] += 1
    diff[r + 1] -= 1

curr = 0
admissible = [0] * (max_temp + 2)

for i in range(1, max_temp + 1):
    curr += diff[i]
    if curr >= k:
        admissible[i] = 1

prefix = [0] * (max_temp + 2)

for i in range(1, max_temp + 1):
    prefix[i] = prefix[i - 1] + admissible[i]

for a, b in queries:
    print(prefix[b] - prefix[a - 1])