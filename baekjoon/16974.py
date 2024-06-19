"""
S(0): P
S(1): B S(0) P S(O) B
...
S(N): B S(N-1) P S(N-1) B

N버거의 X번째를 먼저 구해보자.
5번 버거에서 3번째 값은 4번 버거의 2번째 값과 같고, 
4번 버거의 2번째 값은 3번 버거의 첫번째 값과 같다.

N번 버거의 패티개수는 이전 버거의 패티 개수 * 2 + 1과 같다.
"""
import sys
input = sys.stdin.readline

def getPattyCount(level, nth):
    if level == 0:
        return 1
    
    if nth == 1:
        return 0
    elif nth <= 1 + length[level - 1]:
        return getPattyCount(level - 1, nth - 1)
    elif nth == 2 + length[level - 1]:
        return cnt[level - 1] + 1
    elif nth <= 1 + 2 * length[level - 1]:
        return (cnt[level - 1] + 1) + getPattyCount(level - 1, nth - (length[level - 1] + 2))
    else:
        return cnt[level]

LEVEL, X = map(int, input().split())

length = [1]    # 레벨별 버거의 길이
cnt = [1]       # 레벨별 패티개수

for i in range(1, LEVEL + 1):
    length.append(2 * length[i - 1] + 3)
    cnt.append(2 * cnt[i - 1] + 1)

print(getPattyCount(LEVEL, X))