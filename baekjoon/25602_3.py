"""
1번째날, 
1번캔을 메리가 고르는 경우 - 랑이가 고르는 경우
                        - 랑이가 고르지 않는 경우
        메리가 고르지 않는 경우 - 랑이가 고르는 경우
                            - 랑이가 고르지 않는 경우
"""
import sys
input = sys.stdin.readline

def recur(cur, canA, canB):
    if can[canA] < 0 or can[canB] < 0:
        return -(1 << 60)

    if cur == K:
        return 0
    
    ret = 0
    for i in range(N):
        can[i] -= 1
        for j in range(N):
            can[j] -= 1
            ret = max(ret, recur(cur + 1, i, j) + arrR[cur][i] + arrM[cur][j])
            can[j] += 1
        can[i] += 1

    return ret

N, K = map(int, input().split())        # 캔의 종류 N, 급식 일자 K
can = list(map(int, input().split()))
arrR = [list(map(int, input().split())) for _ in range(K)]
arrM = [list(map(int, input().split())) for _ in range(K)]
ans = recur(0, 0, 0)
print(ans)