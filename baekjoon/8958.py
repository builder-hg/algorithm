import sys
input = sys.stdin.readline

Q = int(input())
while Q:
    Q -= 1

    arr = [''] + list(input().strip())
    cnt = 0     # 가중치 점수
    point = 0   # 총합

    for i in range(1, len(arr)):
        if arr[i] == 'X':
            cnt = 0
            continue

        if arr[i-1] == 'O':
            cnt += 1
        else:
            cnt = 1

        point += cnt


    print(point)