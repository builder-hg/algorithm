import sys
input = sys.stdin.readline

Q = int(input())

while Q:
    Q -= 1
    lst = list(map(int, input().split()))
    N = lst[0]
    arr = lst[1:]
    my_mean = sum(arr) // N
    cnt = 0
    for i in range(N):
        if arr[i] > my_mean:
            cnt += 1

    # print(f"{cnt/N * 100:.3f}")
    print(str(round(cnt/N * 100, 3)) + '%')