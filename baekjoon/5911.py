"""
1번부터 N번까지 쿠폰이 각각 적용 되었을 때, (최대 1,000번)
N개중 가능한 경우를 구한다.                 (최대 1,000번)
=> 1,000 * 1,000 = 1,000,000번으로 완전탐색을 해본다.
"""
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
raw = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N):
    data = []
    pay = raw[i][0] / 2 + raw[i][1]
    if pay <= K:
        tmp += 1
    else:
        pay = 0
    for j in range(N):
        if i == j: continue

        pay += raw[j][0] + raw[j][1]
        if pay <= K:
            tmp += 1
        else:
            pay -= raw[j][0] + raw[j][1]

    ans = max(ans, tmp)
print(ans)