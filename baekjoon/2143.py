"""
[완전탐색]
1. A, B 각각의 부분 배열의 합들이 더해지는 경우를 모두 구한다. 
2. 모든 부분배열의 합을 살펴보며(1 ~ N, 2 ~ N, ..., N : A, B 각각의 부분배열을 모두 구한 후 각 부분배열의 합들이 나오는 경우를 모두 구한다.)

[완전탐색으로 인한 시간초과]
- A의 부분배열을 보는데 N!, B의 부분배열을 보는데 N!, A와 B를 합쳐서 보는데 N! * N!

[시간초과 개선하기]
- 부분배열을 보는 부분을 구간 get이 아닌 점 get으로 바꾼다. O(n) => O(1)

[케이스 살펴보기]
T = 5
A = {1, 3, 1, 2}
B = {1, 3, 2, 0}
prefixA = [0, 1, 4, 5, 7]
prefixB = [0, 1, 4, 6, 6]
countingA = [0, 2, 1, 1]
countingB = [0, 1, 1, 1]
for i in range(len(countingA)):
    countingB[T-i] 
- A의 모든 부분합을 구한다.
- T - (A의 부분합) 을 충족시키는 B의 부분합을 구하고 그 개수를 더한다.
"""
import sys
input = sys.stdin.readline

d = int(input())
ans = 0 

A_N = int(input())
rawA = [0] + list(map(int, input().split()))
prefixA = [0 for _ in range(A_N + 1)]
dict_A = {}

B_N = int(input())
rawB = [0] + list(map(int, input().split()))
prefixB = [0 for _ in range(B_N + 1)]
dict_B = {}

for i in range(1, A_N + 1):
    prefixA[i] = prefixA[i-1] + rawA[i]
for i in range(1, B_N + 1):
    prefixB[i] = prefixB[i-1] + rawB[i]

for i in range(B_N + 1):
    for j in range(i+1, B_N + 1):
        val = prefixB[j] - prefixB[i]
        dict_B[val] = dict_B.get(val, 0) + 1

for i in range(A_N + 1):
    for j in range(i+1, A_N + 1):
        val = prefixA[j] - prefixA[i]
        ans += dict_B.get(d - val, 0)

print(ans)