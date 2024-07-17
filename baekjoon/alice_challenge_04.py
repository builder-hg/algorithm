import sys
input = sys.stdin.readline

def recur(cur, total):
    if not checkEndPoint(cur):
        return 0
    
    if dp[cur] != -1:
        return dp[cur]

    ret = recur(cur + arr[cur][0]) + arr[cur][1]
    ret = max(ret, recur(cur + 1))

    dp[cur] = ret
    return dp[cur]

N = int(input())
arr = []
v = [[] for i in range(N + 1)]
visited = [False for i in range(N + 1)]
for i in range(N - 1):
	a, b = map(int, input().split())
	
	v[a].append(b)
	v[b].append(a)
	
dp = [-1 for _ in range(N)]
print(v)

def checkEndPoint(cur):
	end = True
	for nxt in v[cur]:
		if visited[nxt]:
			continue
			
		end = False

    return 'ans'