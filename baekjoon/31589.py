import sys
input = sys.stdin.readline

N, K = map(int, input().split())
raw = [0] + list(map(int, input().split()))
raw.sort()

s = 0
e = N
cnt = 0
ans = 0
while cnt < K:
    if cnt % 2:
        s += 1
        cnt += 1
    else:
        ans += raw[e] - raw[s]
        e -= 1
        cnt += 1

print(ans)
"""
import sys
input = sys.stdin.readline

def recur(cur, prv, cnt):
    if cnt == K:
        return 0
    
    if cur == N:
        return 0
    
    ret = 0
    if prv == -1:
        ret = max(ret, recur(cur + 1, cur, cnt + 1) + raw[cur])
    else:
        if raw[prv] < raw[cur]:
            ret = max(ret, recur(cur + 1, cur, cnt + 1) + raw[cur] - raw[prv])
        else:
            ret = max(ret, recur(cur + 1, cur, cnt + 1))
    ret = max(ret, recur(cur + 1, prv, cnt))


    return ret

N, K = map(int, input().split())
raw = list(map(int, input().split()))
ans = recur(0, -1, 0)
print(ans)
"""