"""
[문제 풀이 전략]

1. 문제 이해 및 정리
- 막대기둥 개수: N (1<= N <= 1000)
- X좌표와 Y좌표가 N개씩 주어진다. (1 <= X, Y <= 1000)

2. 문제 풀이 방향
- X 좌표를 오름차순으로 정렬하고 싶다. 
=> 창고 리스트를 생성한다 (1000)
=> 리스트[X] = Y를 대입한다.
- Y가 커지면 높이값을 갱신한다. 다음 차례에 올 Y가 작거나 같으면 그대로 유지된다.
- X 좌표를 움직일때마다 새롭게 갱신 혹은 유지되는 Y값들을 더해서 출력한다.
=> 창고 전체를 순회하며 높이값(h)을 갱신 혹은 유지한다
=> if h < list[i], h = list [i]
=> amswer += h
"""
import sys

N = int(input())
warehouse = [0 for _ in range(1010)]
lastX = 0
height = 0
answer = 0
for index in range(N):
    x, y = map(int, sys.stdin.readline().split())
    warehouse[x] = y
    if index == N-1:
        lastX = x

for i in range(1, 1001):
    if height <= warehouse[i]:
        height = warehouse[i]
    print(height)
    answer += height

    if i == lastX + 1:
        break
print(answer)
