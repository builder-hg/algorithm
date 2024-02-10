while True:
    N = int(input())

    if N == 0: break

    revrse = 0
    temp = N

    while temp != 0:
        revrse = revrse * 10 + temp % 10
        temp //= 10

    if N == revrse:
        print("yes")
    else:
        print("no")