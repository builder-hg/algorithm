import sys 
input = sys.stdin.readline

def recur(cur):
    if len(lst) == K:
        tmp = ''
        for item in lst:
            tmp += item
        ans.append(tmp)

        return
    
    if cur == N:
        return

    for i in range(N):
        if visited[i]:
            continue

        visited[i] = True
        lst.append(str(raw[i]))
        recur(cur + 1)

        visited[i] = False
        lst.pop()

N = int(input())
K = int(input())
raw = []
for _ in range(N):
    x = int(input())
    raw.append(x)

lst = []
ans = []
visited = [False for _ in range(N)]
recur(0)

ans = list(set(ans))
print(len(ans))