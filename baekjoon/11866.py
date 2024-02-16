import sys
input = sys.stdin.readline

N, K = map(int, input().split())
visited = [True for _ in range(N + 1)]
visited[0] = False
ans = []
chk = N
cnt = 1
label = 1

while chk:
    idx = label % (N + 1)

    if visited[idx] == False:
        label += 1
        continue

    if cnt == K:
        chk -= 1
        ans.append(str(idx))
        visited[idx] = False
        cnt = 1
        label += 1
        continue


    label += 1
    cnt += 1

text = '<'+', '.join(ans)+'>'
print(text)