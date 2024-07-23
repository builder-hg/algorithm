import sys
input = sys.stdin.readline

N, K = map(int, input().split())    # 인원 N, 제한가 K
raw = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N):                  # 쿠폰을 적용할 선물을 고르는 경우
    arr = [raw[i][0] / 2 + raw[i][1]]
    for j in range(N):
        if i == j:
            continue

        tmp = raw[j][0] + raw[j][1]
        arr.append(tmp)
    arr.sort()
    
    val = 0
    tmp = 0
    for j in range(N):
        val += arr[j]

        if val > K:
            break

        tmp += 1
    ans = max(ans, tmp)

print(ans)
