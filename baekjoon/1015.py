"""
N 길이의 수열 P는 0 ~ N-1의 값으로 이루어져 있다. 

B[P[0]] = A[0] = 2
B[P[1]] = A[1] = 3
B[P[2]] = A[2] = 1

0, 1, 2
1  2  0


A의 배열의 값 중 가장 작은 값부터 +1 씩(초기값 -1)을 부여한다.
"""
import sys
input = sys.stdin.readline

N = int(input())
raw = list(map(int, input().split()))

arr = []
for i in range(N):
    a, b = raw[i], i
    arr.append([a, b])
arr.sort()

ans = [0 for _ in range(N)]
for i in range(N):
    ans[arr[i][1]] = i

print(*ans)