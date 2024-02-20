# 3번 템플릿
import sys
input = sys.stdin.readline

while True:
    raw = list(map(int, input().split()))
    
    if len(raw) == 1 and raw[0] == 0:
        sys.exit()

    K = raw[0]
    arr = raw[1:]
    ans = [0 for _ in range(6)]

    def recur(cur, start):
        # 기저조건 
        if cur == 6:
            print(*ans)
            return

        # 재귀호출
        for i in range(start, len(arr)):
            ans[cur] = arr[i]
            recur(cur + 1, i + 1)

    recur(0, 0)
    print()

