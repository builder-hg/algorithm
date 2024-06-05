import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = list(map(int, input().split()))

ans = (1 << 60)

for i in range(N):
    temp = [0 for _ in range(N)]
    temp[i] = lst[i]

    flag = False
    for j in range(i - 1, -1, -1):
        temp[j] = temp[j + 1] - K
        if temp[j] <= 0:
            flag = True
            break
    
    if flag: continue

    for j in range(i + 1, N):
        temp[j] = temp[j - 1] + K

    cnt = 0
    for j in range(N):
        if temp[j] != lst[j]:
            cnt += 1

    ans = min(ans, cnt)

print(ans)