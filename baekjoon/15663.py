import sys
input = sys.stdin.readline

def recur(cur):
    if cur == M:
        tmp = str(ans[0])
        for i in range(1, M):
            tmp += ' ' + str(ans[i])
        if dic.get(tmp, 0) == 0:
            log.append(tmp)
            dic[tmp] = 1
        return
    
    for i in range(N):
        if visited[i]: continue

        visited[i] = True
        ans[cur] = raw[i]
        recur(cur + 1)

        visited[i] = False

N, M = map(int, input().split())
raw = sorted(list(map(int, input().split())))
visited = [False for _ in range(N)]
ans = [0 for _ in range(N)]
log = []
dic = {}
recur(0)

for item in log:
    print(item)