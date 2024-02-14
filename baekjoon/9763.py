# 풀이과정 설명듣고 작성한거, 내 머리아님, 다시 풀어야함
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

result = 1 << 64

for i in range(N):
    nearest, closet = 1 << 64, 1 << 64
    for j in range(N):
        if i != j:
            distance = abs(arr[i][0] - arr[j][0]) + abs(arr[i][1] - arr[j][1]) + abs(arr[i][2] - arr[j][2])
            if nearest > distance:
                closet = nearest
                nearest = distance
            elif closet > distance:
                closet = distance
    result = min(result, nearest + closet)

print(result)