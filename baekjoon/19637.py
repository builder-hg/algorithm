import sys
input = sys.stdin.readline

def getIndex(K):
    ret = 0
    s = 0
    e = N - 1
    while s <= e:
        mid = (s + e) // 2

        if int(info[mid][1]) < K:
            s = mid + 1
        else:               # info[mid][1] >= K         
            ret = mid
            e = mid - 1

    return ret

N, Q = map(int, input().split())            # 칭호의 개수, 쿼리 개수
info = [list(map(str, input().split())) for _ in range(N)]

while Q:
    Q -= 1

    value = int(input())
    index = getIndex(value)
    print(info[index][0])