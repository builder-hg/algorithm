import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

raw = [0 for _ in range(N + 1)]
for _ in range(Q):
    s, e, k = map(int, input().split())
    raw[s] += k

    if e + 1 > N:
        continue
    raw[e + 1] -= k

print(raw)

prefix = [0 for _ in range(N + 1)]
for i in range(1, N + 1):
    prefix[i] = prefix[i-1] + raw[i]

ans = [0 for _ in range(N + 1)]
for i in range(1, N+1):
    if prefix[i] == prefix[i - 1]:
        ans[i] = prefix[i]
    else:
        ans[i] = prefix[i] - prefix[i-1]

print(prefix)

"""
순서가고려되어야해 raw 에 넣을때부터 고려해서 raw에 넣든 말든하는게 나을듯 ㅠ 
"""