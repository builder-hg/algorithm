import sys
input = sys.stdin.readline

def recur(cur, start):
    if cur == M:
        tmp = str(log[0])
        for i in range(1, M):
            tmp += ' ' + str(log[i])
        if dic.get(tmp, 0) == 0:
            dic[tmp] = 1
            ans.append(tmp)
        return
    
    for i in range(start, N):
        if visited[i]: continue

        visited[i] = True
        log[cur] = raw[i]
        recur(cur + 1, i + 1)

        visited[i] = False

N, M = map(int, input().split())
raw = sorted(list(map(int, input().split())))
visited = [False for _ in range(N)]
log = [0 for _ in range(N)]
ans = []
dic = {}
recur(0, 0)

for item in ans:
    print(item)