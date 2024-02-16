"""
0. 특징파악하기
- 6 * X  + 3 * Y = N
- X + Y 가 기존 X + Y 보다 작다면 갱신한다.
- 위 식을 성립하지 못한다면 -1을 출력한다.
"""
import sys
input = sys.stdin.readline

N = int(input())
cnt = 5000

range_5kg = N // 5
range_3kg = N // 3

for i in range(range_5kg + 1):
    for j in range(range_3kg + 1):
        val = 5 * i + 3 * j 
        if val == N:
            if i + j < cnt:
                cnt = i + j

if cnt == 5000:
    print(-1)
else:
    print(cnt)