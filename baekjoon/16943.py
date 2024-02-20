"""
1. 접근하기
1) A로 만들 수 있는 모든 경우의 수를 구한다. 이 때 제일 앞자리가 0이 되면 안된다.
2) 각각의 경우의 수를 B와 비교한다. B보다 작고 이전 값보다 크다면 계속 갱신한다.
3) 템플릿 2
"""
import sys
input = sys.stdin.readline

A, B = map(int, input().split())
arr = list(str(A))
ans = [0 for _ in range(len(arr))]
visited = [False for _ in range(len(arr))]
val = -1

def recur(cur):
    global val
    # 기저조건
    if cur == len(arr):
        temp = ''
        for i in range(len(ans)):
            if i == 0 and ans[i] == '0':
                return
            temp += ans[i]
        temp = int(temp)

        if temp < B:
            if temp > val:
                val = temp
        return

    # 재귀호출
    for i in range(len(arr)):
        if visited[i]:
            continue

        visited[i] = True
        ans[cur] = arr[i]
        recur(cur+1)
        visited[i] = False

recur(0)

print(val)