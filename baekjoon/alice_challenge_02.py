import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [0] + list(map(int, input().split()))
for _ in range(K):
    s, b, c = map(int, input().split())
    e = b + 1
    idx = c - 1
    
    tmp = sorted(arr[s:e])
    print(tmp[idx])
