"""
1. 완전탐색
- [0, 0]부터 [N, M] 까지 N*M개의 경우에서 64칸씩 살펴본다.
- 시간은 50 * 50 * 64 = 6400

2. 특징
1) 초깃값이 'W'
- dx: 0 혹은 짝수일 때, dy가 0 혹은 짝수인 지점은 W, 그 외에는 'B'
- dx: 홀수일 때, dy가 0 혹은 짝수인 지점은 'B', 그 외에는 'W'
2) 초깃값이 'B'
- dx: 0혹은 짝수일 때,dy가 0 혹은 짝수인 지점은 'B' 그 외에는 'W'
- dx: 홀수일 때, dy가 0혹은 짝수인 지점은 'W' 그 외에는 'B'
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(input().strip()) for _ in range(N)]
min_value = 1 << 64
init = ''
other = ''


# 앞으로 접근하기
for sx in range(N-7):# 시작점 지정
    for sy in range(M-7):# 시작점 지정
        # 초깃값 설정
        if arr[sx][sy] == 'W': 
            init = 'W'
            other = 'B'
        else:
            init = 'B'
            other = 'W'
        cnt = 0

        up_x = -1
        up_y = -1
        # 해당 시작점 sx, sy에서 체커판을 순회한다.
        for dx in range(sx, sx + 8):
            up_x += 1
            for dy in range(sy, sy + 8):
                up_y += 1
                if up_x == 0 or up_x % 2 == 0:  # dx가 0 혹은 짝수일 때
                    if up_y == 0 or up_y % 2 == 0:  # dy가 0 혹은 짝수인 지점에서
                        if arr[dx][dy] != init: # 초깃값과 다르다면 다시 색칠해야한다.
                            cnt += 1
                    else:                   
                        if arr[dx][dy] != other: #초깃값과 동일하다면 다시 색칠해야 한다.   
                            cnt += 1
                else: # dx가 홀수일때 dy가 0 혹은 짝수인 지점은 other, 그 외에는 init
                    if up_y == 0 or up_y % 2 == 0:
                        if arr[dx][dy] != other:
                            cnt += 1
                    else:
                        if arr[dx][dy] != init:
                            cnt += 1

        reverse_value = 64 - cnt
        diff = min(cnt, reverse_value)                    
        min_value = min(min_value, diff)

print(min_value)