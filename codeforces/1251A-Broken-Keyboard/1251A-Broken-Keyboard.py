# the last element
    if cnt % 2 != 0:
        res.add(typed[i])
    res = list(res)
    res.sort()
    print("".join(res))