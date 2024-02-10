"""
0. 관찰
1행: 1
- 1
2행: 6
- 2 ~ 7
3행: 12 
- 8 ~ 19
- 1+7 ~ 12+7
4행: 18
- 20 ~ 37
5행: 24
- 38 ~ 61

시작번호: 1, 2, 8, 20, 38
1. 특징파악
1) 행파악
n = 0
while True:
    n += 1
    if 1+ (n-1) * 6 > 10:
        print(n)
        sys.exit()
2)
"""
import sys 
input = sys.stdin.readline

N = int(input())
end = 1
cnt = 1

while N > end:
    end += 6 * cnt
    cnt += 1

print(cnt)