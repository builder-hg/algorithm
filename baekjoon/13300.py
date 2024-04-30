import sys
input = sys.stdin.readline

N, K = map(int, input().split())
cnt = 0
female = {}
male = {}
for _ in range(N):
    a, b = map(int, input().split())
    if a == 1: # 남학생
        male[b] = male.get(b, 0) + 1
    else:
        female[b] = female.get(b, 0) + 1

for k, v in female.items():
    if v % K == 0:
        cnt += (v // K)
    else:
        cnt += (v // K) + 1

for k, v in male.items():
    if v % K == 0:
        cnt += (v // K)
    else:
        cnt += (v // K) + 1

print(cnt)