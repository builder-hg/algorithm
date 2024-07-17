import sys
input = sys.stdin.readline

def recur(cur, start):
    if cur == M:
        print(*arr)
        return
    
    for i in range(start, N + 1):
        arr[cur] = i
        recur(cur + 1, i)

N, M = map(int, input().split())
arr = [0 for _ in range(M)]

recur(0, 1)