import sys
input = sys.stdin.readline

def getValue():
    ret = 0
    for i in range(N):
        ret += int(arr[i]) * 10 ** (N - i - 1)
    return ret

def recur(cur):
    global ans

    if cur == N:
        tmp = getValue()
        if today >= tmp:
            return

        ans = min(ans, tmp)

        return

    for i in range(N):
        if visited[i]:
            continue

        visited[i] = True
        arr[cur] = raw[i]

        recur(cur + 1)
        visited[i] = False

today = int(input())
raw = list(str(today))
N = len(raw)
visited = [False for _ in range(N)]
arr = [0 for _ in range(N)]
ans = (1 << 60)
recur(0)

print(ans)