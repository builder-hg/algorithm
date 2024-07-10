import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
query = []
for i in range(Q):
    s, e, color = map(int, input().split())
    query.append([s, e, color])
query = query[::-1]
print(query)
