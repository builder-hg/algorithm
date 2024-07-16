import sys
import copy
input = sys.stdin.readline

def getPoint():
    ret = 0
    count = copy.deepcopy(can)      # 캔의 개수가 담긴다
    for i in range(K):              # i는 일자를 의미한다.
        count[choice[i]] -= 1       # choice[i]는 i날짜에 선택된 캔의 위치를 의미한다. 
        if count[choice[i]] < 0:
            return -(2 << 60)
        
        ret += arrR[i][choice[i]]   # 랑이의 만족도를 더한다.
        ret += arrM[i][choice[i]]   # 메리의 만족도를 더한다.

    return ret

def choiceCan(cur):
    global ans

    if cur == K:                # 캔 K개를 선택한 경우
        ans = max(ans, getPoint())  # 기존 만족도와 새로운 만족도를 비교하여 갱신한다.
        return
    
    for i in range(N):          # 캔을 중복하여 고를 수 있다.
        choice[cur] = i         # choice에는 캔의 위치가 저장된다.
        choiceCan(cur + 1)

N, K = map(int, input().split())
can = list(map(int, input().split()))
arrR = [list(map(int, input().split())) for _ in range(K)]
arrM = [list(map(int, input().split())) for _ in range(K)]

choice = [0 for _ in range(K)]
ans = 0
choiceCan(0)
print(ans)