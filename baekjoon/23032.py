"""
[문제풀이전략]
1. 문제 이해 및 정리
- 학생 N명(2<=N<=2,000), 스테이크 W(1<=W<=10,000)
- 두 그룹의 합의 차이를 최소로 한다. 최소가 되는 그룹의 합을 구한다.
- 만약 최소가 되는 경우가 여러개있다면 합이 가장 큰 두 그룹을 고른다.

2. 문제 풀이 방향
6, sum=18
2 1 5 2 4 4
  s
      e
1) 2, 16
2) 3, 15
3) 8, 10
4) 10, 8
5) 8, 8

6, sum=54
5 10 5 3 20 11
       s
         e
1) 5, 49
2) 15, 39
3) 20, 34
4) 23, 31 -> 저장될 데이터
5) 43, 11 -> 저장연산이 실행될 지점
6) 38, 11
7) 28, 11
8) 23, 11
"""
# lst= [2,1,5,2,4,4]
# for i in range(6):
#     for j in range(i+1, 6):
#         for k in range(j+1, 6):
#             for l in range(k+1, 6):
#                 print(lst[i], lst[j], lst[k] ,lst[l])

import sys

N = int(input())    # 학생 수
lst = [0] + list(map(int, sys.stdin.readline().split())) + [0]    
splitter = 1
diff = 1 << 64
ans = 0 
while splitter < N:  # splitter
    left = splitter
    right = splitter + 1
    totalA = lst[left]
    totalB = lst[right]

    while left >= 1 and right <= N:
        if totalA <= totalB:    # 좌측 구간의 길이를 늘리는 경우
            if diff > totalB - totalA:  # 구간의 차이값이 기존에 구한 차이값보다 작은경우     
                diff = totalB - totalA  # 차이값 갱신
                ans = totalA + totalB  # 답 갱신(스테이크 총합)
            elif diff == totalB - totalA:
                diff = totalB - totalA  # 차이값 갱신
                ans = max(ans, totalA + totalB)  # 차이값이 동일한 경우 스테이크 합이 큰 경우를 선택한다.
            left -= 1
            totalA += lst[left]
        else:                   # 우측 구간의 길이를 늘리는 경우
            if diff > totalA - totalB:  # 구간의 차이값이 기존에 구한 차이값보다 작은경우     
                diff = totalA - totalB  # 차이값 갱신
                ans = totalA + totalB  # 답 갱신(스테이크 총합)
            elif diff == totalA - totalB:
                diff = totalA - totalB  # 차이값 갱신
                ans = max(ans, totalA + totalB)  # 차이값이 동일한 경우 스테이크 합이 큰 경우를 선택한다.
            right += 1
            totalB += lst[right]

    splitter += 1

print(ans)

