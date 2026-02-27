#https://codeforces.com/problemset/problem/2126/D
#D. This Is the Last Time
t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    
    casinos = []
    for _ in range(n):
        l, r, reali = map(int, input().split())
        casinos.append((l, r, reali))
    
    # Sort by l
    casinos.sort()
    
    current = k
    
    for l, r, reali in casinos:
        if l <= current <= r:
            if reali > current:
                current = reali
    
    print(current)
