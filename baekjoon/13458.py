# 9
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
R, O = map(int, input().split()) #required, optional
cnt = 0

for i in range(N):
    # 필수 감독
    if arr[i] - R <= 0:
        cnt += 1
        continue

    cnt += 1
    if (arr[i] - R) % O > 0:
        cnt += ((arr[i] - R) // O + 1)
    else:
        cnt += ((arr[i] - R) // O)

print(cnt)

