import sys
from collections import deque
input = sys.stdin.readline

def traceback(cur):
    ans = []
    now = cur
    ans.append(K)

    for _ in range(dis):
        ans.append(arr[now])
        now = arr[now]

    print(*ans[::-1])
    return


N, K = map(int, input().split())
que = deque()
dis = 0
visited = [False for _ in range(100100)]
arr = [0 for _ in range(100100)]
flag = False

add = [-1, 1, 0]
mul = [1, 1, 2]

que.append(N)
visited[N] = True
while len(que) > 0:
    sz = len(que)

    for _ in range(sz):
        cur = que[0]
        que.popleft()

        if cur == K:
            print(dis)
            traceback(K)
            flag = True
            
        if flag: break

        for i in range(3):
            nxt = mul[i] * cur + add[i]

            if nxt >= 0 and nxt <= 100000 and not visited[nxt]:
                que.append(nxt)
                arr[nxt] = cur
                visited[nxt] = True

    if flag:break

    dis += 1
