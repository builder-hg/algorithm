import sys
input = sys.stdin.readline
N, M = map(int, input().split())
lst = [0] + list(map(int, input().split()))
prefix_lst = [0 for _ in range(N+1)]
for i in range(1, N+1):
    prefix_lst[i] = prefix_lst[i-1] + lst[i]

while M:
    M -= 1
    s, e = map(int, input().split())
    ans = prefix_lst[e] - prefix_lst[s-1]
    print(ans)