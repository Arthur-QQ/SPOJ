for _ in range(10):
    s = input()
    f = 0
    for c in s:
        if c in ['T', 'D', 'L', 'F']:
            f += 1
    print(2 ** f)
