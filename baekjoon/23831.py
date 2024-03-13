import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())
A, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def recur(cur, loc, prev, cnt_a, cnt_b): # cur: 날짜, loc: 장소(0~3), prev: 이전 장소, cnt_a: 정독실 및 소학습실 자습 회수, total: 만족도
    if loc == 2 and prev == 2:
        return -(1 << 60)
    
    if loc == 3:
        cnt_b += 1
    
    if cnt_b > A:
        return -(1 << 60)

    if cur == N:
        if cnt_a < B:
            return -(1 << 60)
        
        return 0
    
    if dp[cur][loc][prev][cnt_a][cnt_b] != -1:
        return dp[cur][loc][prev][cnt_a][cnt_b]

    ret = -(1 << 60)

    ret = max(ret, recur(cur + 1, 0, loc, cnt_a + 1, cnt_b) + arr[cur][0])
    ret = max(ret, recur(cur + 1, 1, loc, cnt_a + 1, cnt_b) + arr[cur][1])
    ret = max(ret, recur(cur + 1, 2, loc, cnt_a, cnt_b) + arr[cur][2])
    ret = max(ret, recur(cur + 1, 3, loc, cnt_a, cnt_b) + arr[cur][3])

    dp[cur][loc][prev][cnt_a][cnt_b] = ret
    return dp[cur][loc][prev][cnt_a][cnt_b]

dp = [[[[[-1 for _ in range(A + 1)] for _ in range(B + 1)] for _ in range(4)] for _ in range()]]
ans = recur(0, 0, 0, 0, 0, 0)
print(ans)