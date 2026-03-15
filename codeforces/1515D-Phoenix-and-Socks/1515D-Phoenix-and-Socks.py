from collections import Counter
t = int(input())
for _ in range(t):
    n, l, r = map(int, input().split())
    c = list(map(int, input().split()))
    
    left = Counter(c[:l])
    right = Counter(c[l:])
    
    # remove already matched pairs
    for color in list(left.keys()):
        m = min(left[color], right[color])
        left[color] -= m
        right[color] -= m
        l -= m
        r -= m
    
    # ensure left is larger
    if l < r:
        left, right = right, left
        l, r = r, l
    
    cost = 0
    diff = (l - r) // 2
    
    # use duplicate colors
    for color in left:
        while diff > 0 and left[color] >= 2:
            left[color] -= 2
            diff -= 1
            cost += 1
    
    # remaining flips
    cost += diff
    
    # recolor remaining mismatches
    remaining = l + r - 2*((l - r)//2 - diff)
    cost += remaining // 2
    
    print(cost)