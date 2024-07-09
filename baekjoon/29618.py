import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

"""
2차원 배열을 고려한 imos
"""

raw = [[] for _ in range(N + 1)]
for i in range(1, Q + 1):
    s, e, k = map(int, input().split())

    raw[s].append([i, k])
    if e + 1 <= N:
        raw[e + 1].append([i, -k])

print(raw)

for i in range(1, N + 1):
    if raw[i - 1] != []:
        raw[i].extend(raw[i - 1])

    raw[i].sort()

print(raw)

# prefix = [0 for _ in range(N + 1)]
# for i in range(1, N + 1):
#     prefix[i] = prefix[i-1] + raw[i]

# ans = [0 for _ in range(N + 1)]
# for i in range(1, N+1):
#     if prefix[i] == prefix[i - 1]:
#         ans[i] = prefix[i]
#     else:
#         ans[i] = prefix[i] - prefix[i-1]

# print(prefix)
