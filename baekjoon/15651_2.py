import sys
input = sys.stdin.readline

def recur(cur):
    if cur == M:
        print(*arr)
        return
    
    for i in range(1, N + 1):
        arr[cur] = i
        recur(cur + 1)

N, M = map(int, input().split())
arr = [0 for _ in range(M)]

recur(0)