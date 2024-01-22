# 전체 좌표들을 담은 리스트를 생성한다.
# 살펴볼 구간을 줄인다. 기준을 y로 잡고 y1과 y2 사이 혹은 y1과 y3 사이, ... yn-1과 yn사이를 살펴보며
# 줄여진 구간내에 y값을 가진 x의 개수(cntX)가 N//2 이상이라면 
# cntX - 3만큼(직사각형이 될 수 있는 경우의 수) 직사각형의 넓이를 구해본다.
# 넓이 중 가장 작은 값을 저장해서 출력한다.
import sys

N = int(input()) # 좌표의 개수
point_wrapper = []  # 주어진 좌표를 담는다. 2차원 배열로 담으며 x, y의 정보가 담긴다.
y_wrapper = []
ans = 1 << 64       # 직사각형 너비의 초기값
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    point_wrapper.append([x, y])
    y_wrapper.append(y)
y_wrapper.sort()
# y를 기준으로 살펴볼 구간은 다음과 간다.
#   주어진 y좌표들을 순회하며 자기자신을 포함하여 가능한 구간들(yi와 yi+1 사이가 가능한 구간이다)을 탐색한다.
y_section = []
for i in range(N):
    for j in range(i, N):
        if [y_wrapper[i],  y_wrapper[j]] in y_section: # 중복된 부분들은 제거한다. (동일하기에 삭제한다.)
            continue
        y_section.append([y_wrapper[i], y_wrapper[j]])

for i in range(len(y_section)):
    ys, ye = y_section[i]   # 살펴볼 y의 구간을 설정한다.
    satisfied_lstX = []
    for j in range(len(point_wrapper)): # 해당 구간의 놓인 x좌표를 저장한다.
        checkY = point_wrapper[j][1]
        if ys <= checkY <= ye:
            satisfied_lstX.append(point_wrapper[j][0])
    satisfied_lstX.sort()
    if 2 * len(satisfied_lstX) < N:     # 구간에 놓인 좌표의 개수가 조건을 만족하지않는다면 넘어간다.
        continue

    for j in range(len(satisfied_lstX) - N//2 + 1): # 구간 내 직사각형이 될 수 있는 경우만큼 순회한다.
    # 직사각형들의 너비를 대소비교하며 값을 갱신한다.
        new_area = (ye - ys + 2) * (satisfied_lstX[j+N//2-1] - satisfied_lstX[j] + 2)
        ans = min(ans, new_area)

print(ans)