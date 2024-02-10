import sys
input = sys.stdin.readline

N, C = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()

s = 1 # 공유기간의 최소간격
e = arr[N-1] - arr[0]   # 공유기간의 최대간격
ans = 0

while s <= e:
    # 공유기간의 적정거리를 이진탐색으로 추려나가본다.
    mid = (s + e) // 2  
    now = arr[0]    # 처음 공유기를 설치할 위치
    cnt = 1         # 설치한 공유기 개수

    for i in range(1, N):
        if arr[i] >= now + mid: # 첫시작점 + 이진탐색으로 구한 공유기 거리를 더하여 새로운 공유기 설치 위치 탐색
            now = arr[i]
            cnt += 1
        
    if cnt >= C:
        s = mid + 1
        ans = mid 
    else:
        e = mid - 1

print(ans)