"""
입력의 첫 줄에는 테스트 케이스의 개수 T
강의 서쪽과 동쪽에 있는 사이트의 개수 정수 N, M (0 < N ≤ M < 30)
"""
import sys
input = sys.stdin.readline

Q = int(input())

def recur(cur, cnt): 
    if cnt > N:
        return -(1 << 60)
    
    if cur == M:
        if cnt == N:
            return 1

        return -(1 << 60)
    
    if dp[cur][cnt] != -1:
        return dp[cur][cnt]

    ret = 0
    ret += max(0, recur(cur + 1, cnt + 1))
    ret += max(0, recur(cur + 1, cnt))
    dp[cur][cnt] = ret

    return dp[cur][cnt]

while Q:
    Q -= 1
    N, M = map(int, input().split())
    dp = [[-1 for _ in range(31)] for _ in range(31)]
    ans = recur(0, 0)
    print(ans)