import sys
input = sys.stdin.readline

Q = int(input())
while Q:
    Q -= 1

    w, h, n = map(int, input().split())
    arr = [[0 for _ in range(w+2)] for _ in range(h+2)]
    print(arr)
    for i in range(n):
        x, y = map(int, input().split())
        x += 1 
        y += 1
        arr[y][x] = 1

    for i in range(1, h+1):
        for j in range(1, w+1):
            if arr[i][j] == 0:
                continue

            while True:
                arr[i+1][j]
                arr[i+1][j]

