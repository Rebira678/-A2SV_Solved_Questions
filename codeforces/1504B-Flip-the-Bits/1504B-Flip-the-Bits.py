# Step 1: Identify all prefix indices where count(0) == count(1)
    # We add n to handle the boundary cases
    breakpoints = []
    count0 = 0
    count1 = 0
    for i in range(n):
        if a[i] == '0':
            count0 += 1
        else:
            count1 += 1
        
        if count0 == count1:
            breakpoints.append(i)

    possible = True
    last_bp = -1

    # Step 2: Check each segment between breakpoints
    for bp in breakpoints:
        segment_a = a[last_bp + 1 : bp + 1]
        segment_b = b[last_bp + 1 : bp + 1]
        
        # In any valid segment, a must either match b exactly 
        # OR be the bitwise inverse of b.
        is_same = segment_a == segment_b
        is_inverse = all(a_char != b_char for a_char, b_char in zip(segment_a, segment_b))
        
        if not (is_same or is_inverse):
            possible = False
            break
        last_bp = bp
        
    # Step 3: Check the remaining suffix after the last valid breakpoint
    # If there's a trailing part that doesn't match and can't be flipped
    if last_bp < n - 1:
        if a[last_bp + 1:] != b[last_bp + 1:]:
            possible = False

    print("YES" if possible else "NO")