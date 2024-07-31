import sys
input = sys.stdin.readline

N = int(input())
arr = [0] + sorted(list(map(int , input().split())))

prefix = [0 for _ in range(N + 1)]
for i in range(1, N + 1):
    prefix[i] = prefix[i - 1] + arr[i]

print(sum(prefix))