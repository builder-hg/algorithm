def find_minimum_area(points):
    min_area = float('inf')  # 최소 넓이를 저장할 변수 초기화

    for i in range(len(points)):  # 모든 점에 대해 왼쪽 위 꼭짓점을 선택
        for j in range(i + 1, len(points)):  # 모든 점에 대해 오른쪽 아래 꼭짓점을 선택
            # 왼쪽 위와 오른쪽 아래 꼭짓점을 지정하여 직사각형의 넓이 계산
            area = abs(points[i][0] - points[j][0]) * abs(points[i][1] - points[j][1])
            # 내부에 있는 점의 개수가 N/2 이상인 경우만 고려
            if area < min_area and sum(1 for x, y in points if points[i][0] <= x <= points[j][0] and points[i][1] <= y <= points[j][1]) >= len(points) / 2:
                min_area = area  # 최소 넓이 갱신

    return min_area

# 입력 받기
N = int(input())  # 점의 개수
points = []  # 점의 좌표를 저장할 리스트 초기화
for _ in range(N):
    x, y = map(int, input().split())  # 점의 좌표 입력 받기
    points.append((x, y))

print(points)
# 최소 넓이 계산
min_area = find_minimum_area(points)

# 결과 출력
print(min_area)