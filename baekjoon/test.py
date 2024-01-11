def pows(n, m):
    if m == 0:
        return 1
    ret = pows(n, m//2)
    print("n과 m은", n, m)
    print("ret는", ret)
    if m % 2 == 0:
        return ret * ret
    else:
        return ret * ret * n

ans = pows(2,3)
print(ans)