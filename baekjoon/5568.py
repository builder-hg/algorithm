import sys
input = sys.stdin.readline

def recur(cur, cnt):
	if cur == N: # 끝까지 다 살펴본 경우
		if cnt != K:
			return
		
		tmp = ''
		for i in range(cnt):
			tmp += str(arr[i])
		ans.append(tmp)
		return

	for i in range(N):
		if visited[i]:
			continue
		visited[i] = True
		arr[cur] = i
		recur(cur + 1)
		visited[i] = False


N = int(input())
K = int(input())
raw = []
for _ in range(N):
    a = int(input())
    raw.append(a)

arr = [0 for _ in range(N)]
visited = [False for _ in range(N)]
ans = []
recur(0, 0)
print(ans)
print(len(ans))