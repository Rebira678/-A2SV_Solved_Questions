# Process the Blue sequence
    m = int(input())
    b = list(map(int, input().split()))
    
    max_b = 0
    current_b = 0
    for x in b:
        current_b += x
        if current_b > max_b:
            max_b = current_b
            

    print(max_r + max_b)