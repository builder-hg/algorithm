import sys
input = sys.stdin.readline

def recur(cur):
    if cur == M:
        tmp = str(log[0])
        for i in range(1, M):
            tmp += ' ' + str(log[i])
        if dic.get(tmp, 0) == 0:
            dic[tmp] = 1
            ans.append(tmp)

        return
    
    for i in range(N):
        log[cur] = raw[i]
        recur(cur + 1)

N, M = map(int, input().split())
raw = sorted(list(map(int, input().split())))
log = [0 for _ in range(N)]
ans = []
dic = {}
recur(0)

for item in ans:
    print(item)