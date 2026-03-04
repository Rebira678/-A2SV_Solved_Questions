# Step 1: ensure a[i] < b[i]
    for i in range(n):
        if a[i] > b[i]:
            a[i], b[i] = b[i], a[i]
            ops.append((3, i + 1))  # 1-based index

    # Step 2: sort a with bubble sort
    for i in range(n):
        for j in range(n-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                ops.append((1, j + 1))

    # Step 3: sort b with bubble sort
    for i in range(n):
        for j in range(n-1):
            if b[j] > b[j+1]:
                b[j], b[j+1] = b[j+1], b[j]
                ops.append((2, j + 1))

    # Output
    print(len(ops))
    for op in ops:
        print(op[0], op[1])