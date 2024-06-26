import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
que = deque([i for i in range(1, N + 1)])

ans = 0
for target in arr:
    while True:
        if que[0] == target:
            que.popleft()
            break
        else:
            if que.index(target) < (len(que) / 2):
                while que[0] != target:
                    que.append(que.popleft())
                    ans += 1
            else:
                while que[0] != target:
                    que.appendleft(que.pop())
                    ans += 1

print(ans)