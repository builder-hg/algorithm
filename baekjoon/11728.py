"""
[문제풀이전략]
1. 문제 이해 및 정리
- 정렬된 두 배열 A, B
- A의 크기 N, B의 크기 M (1<= N, M <= 1,000,000)
- 수열의 원소는 절댓값이 10^9보다 작거나 같다.
- 출력: 두 배열을 합친 후 정렬한 결과를 출력한다.

2. 문제 풀이 방향
?) 왜 이 문제가 투포인터 숙제일까.
?) 투포인터는 후보군을 제거하거나 늘리는게 핵심이라고 생각한다.
    이 문제랑 어떻게 접목시킬까 
"""
# 투포인터랑 전혀 상관없어 보이는(내 생각에는) 정렬 구현
# import sys
# N, M = map(int, sys.stdin.readline().split())
# list_x = list(map(int, sys.stdin.readline().split()))
# list_y = list(map(int, sys.stdin.readline().split()))
# list_all = list_x + list_y
# idx = 1
# cnt = 0
# while True:
#     if list_all[idx] < list_all[idx - 1]:
#         list_all[idx-1], list_all[idx] = list_all[idx], list_all[idx - 1]
#         cnt += 1
#     idx += 1
#     if idx == (N+M):
#         if cnt == 0:
#             break
#         idx = 1
#         cnt = 0
# print(*list_all)

# 투 포인터로 접근하기
import sys
N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split())) 
B = list(map(int, sys.stdin.readline().split())) 
ans = []
s = 0
x = 0
while s < N and x < M:
    if A[s] <= B[x]:
        ans.append(A[s])
        s += 1 
    else:
        ans.append(B[x])
        x += 1

if s == N:
    # x를 돈다.
    for i in range(x, M):
        ans.append(B[i])
else:
    for i in range(s, N):
        ans.append(A[i])


print(*ans)