"""
// 집의 개수가 짝수(N)일 때, N/2번째부터 N/2+1 번째까지 거리가 최소
1   5 7 9
 x
1   3 5 7 => 16
  x
2   2 4 6 => 14
   x
3   1 3 5 => 12
    x
4   0 2 4 => 10
     x  
5   1 1 3 => 10
      x 
6   2 0 2 => 10

// 집의 개수(N)가 홀수일 때, N/2의 몫 + 1 번째가 거리가 최소
+1-1-1-1-1 => -3
+1+1-1-1-1 => -1
+1+1+1-1-1 => +1
1   5 7 9 11
 x
1   4 6 8 10 => 29
      x
6   2 0 2 4 => 12
"""
import sys

N = int(input())
position = []
position = sorted(list(map(int,sys.stdin.readline().split())))
index: int
answer: int

if N % 2:
    # 홀수인 경우
    answer = position[(N//2)]
else:
    # 짝수인 경우
    answer = position[(N//2)-1]

print(answer)