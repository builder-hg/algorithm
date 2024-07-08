import sys
input = sys.stdin.readline

N = int(input())
raw = [0 for _ in range(1000002)]
for _ in range(N):
    s, e = map(int, input().split())
    raw[s] += 1
    raw[e + 1] -= 1

prefix = [0 for _ in range(1000001)]
for i in range(1, 1000001):
    prefix[i] = prefix[i - 1] + raw[i]

M = int(input())
arr = list(map(int, input().split()))
for i in range(M):
    print(prefix[arr[i]])