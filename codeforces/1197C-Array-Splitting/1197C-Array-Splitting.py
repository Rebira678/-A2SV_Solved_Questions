# If only one subarray
if k == 1:
    print(a[-1] - a[0])
else:
    diffs = []
    
    for i in range(1, n):
        diffs.append(a[i] - a[i-1])
    
    diffs.sort(reverse=True)
    
    total = a[-1] - a[0]
    
    # subtract largest (k-1) gaps
    for i in range(k-1):
        total -= diffs[i]
    
    print(total)