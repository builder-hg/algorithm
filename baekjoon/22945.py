"""
[문제풀이전략]
1. 문제 이해 및 정리
- 개발자 수 N, 하나의 팀을 만들기 위한 인원 2
- 2<=N<=100,000 , 1<=x<=10,000 (능력치는 정수)
- 팀의 능력치: (개발자 A와 개발자 B 사이에 존재하는 다른 개발자 수) × min(개발자 A의 능력치, 개발자 B의 능력치)
- 팀 능력치의 최대값 구하기

2. 아이디어
>  구간의 길이가 길고, 양 끝 지점의 값의 최소값이 클수록 유리하다. 
1)
1 4 2 5 2 1 3
s
            e
이때 ans = min(lst[s],lst[e]) * (e - s - 1) = 5
lst[s]와 lst[e]중 작은 값을 후보에서 제외시킨다.
2)
4 2 5 2 1 3
s
          e
ans = 4* 3 = 12
3)
4 2 5 2 1
s
        e
ans = 3 * 1 = 3
4)
4 2 5 2
s
      e
ans = 2 * 2 = 4 
5)
4 2 5
s
    e 
ans = 1 * 4 = 4

3. 문제 풀이 방향
"""
# 완전탐색
# N = 7
# lst = [1,4,2,5,2,1,3]
# ans = 0
# for i in range(N-2):
#       for j in range(i+2, N):
#             leng = j - i - 1
#             minV = min(lst[i], lst[j])
#             ans = max(ans, leng * minV)

# print(ans)
import sys

N = int(input())                                      # 개발자 인원
lst = list(map(int, sys.stdin.readline().split()))    # 능력치를 담은 리스트
ans = 0
s = 0       # 시작지점
e = N-1     # 끝지점
while e - s > 1:
      leng = e - s - 1
      minV = min(lst[s], lst[e])
      ans = max(ans, leng * minV)

      if lst[s] <= lst[e]:
            s += 1
      else:
            e -= 1

print(ans)
