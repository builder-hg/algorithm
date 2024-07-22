import sys
input = sys.stdin.readline

N, D = map(int, input().split())
raw = [[] for _ in range(3)]    # raw[1]에는 몬스터의 정보가, raw[2]에는 장비 정보가 저장된다.
for _ in range(N):
    idx, val = map(int, input().split())
    raw[idx].append(val)
for i in range(3):              # 몬스터와 장비 정보가 정렬된다.
    raw[i].sort()

ans = 0
cnt = 0
ability = D

idx = 0
while idx < len(raw[1]):
    if raw[1][idx] < ability:
        ans += 1
        ability += raw[1][idx]
        idx += 1
    else:
        if cnt == len(raw[2]):
            break

        ability *= raw[2][cnt]
        ans += 1
        cnt += 1

while cnt != len(raw[2]):
    cnt += 1
    ans += 1

print(ans)

"""
상황별 처리
01) 처리할 수 있는 몬스터가 있는 경우
02) 처리할 수 있는 몬스터가 없고 장비가 있는 경우
03) 처리할 수 있는 몬스터도 장비도 없는 경우
import sys
input = sys.stdin.readline

def getIndex(val):      # 해당 능력치로 이길 수 있는 몬스터 중 가장 강한 몬스터의 위치를 반환한다.
    ret = 0

    s = 0
    e = len(raw[1]) - 1
    while s <= e:
        mid = (s + e) // 2

        if raw[1][mid] < val:
            ret = mid
            s = mid + 1
        else:
            e = mid - 1

    return ret

N, D = map(int, input().split())
raw = [[] for _ in range(3)]    # raw[1]에는 몬스터의 정보가, raw[2]에는 장비 정보가 저장된다.
for _ in range(N):
    idx, val = map(int, input().split())
    raw[idx].append(val)
for i in range(3):              # 몬스터와 장비 정보가 정렬된다.
    raw[i].sort()

ability = D                     # 내가 가진 능력치
visited = [False for _ in range(len(raw[1]))]   # 몬스터가 있는 곳 방문 여부
start = 0
ans = 0                         # 방문 횟수
cnt = 0                         # 장비 사용횟수 
while True:
    cur = getIndex(ability)

    if len(raw[1]) and raw[1][cur] < ability and not visited[cur]:            # 처리할 수 있는 몬스터가 있는 경우
        for i in range(start, cur + 1):                         # 처리가능한 몬스터를 모두 처리한다.
            visited[i] = True                                   # 처리했다면 체크한다.
            ans += 1
            ability += raw[1][i]
        start = cur + 1
        continue

    if cnt != len(raw[2]):          # 처리할 수 있는 몬스터가 없고 장비가 있는 경우
        ability *= raw[2][cnt]      # 장비를 사용한다.
        ans += 1                    
        cnt += 1                    
        continue

    break

print(ans)


"""
"""
전략: 
01) 내가 현재 가진 전투력으로 이길 수 있는 몬스터를 해치워 전투력을 높인다.
02) 현재의 전투력으로 남은 몬스터를 없앨 수 없다면 장비 전투력을 곱해준다.
03) 01)과 02)를 반복한다.

접근:
01) 몬스터와 장비에 대한 정보가 담긴 배열을 만든다. 1인덱스에는 몬스터에 관한, 인덱스 2에는 장비에 관한 정보가 담긴다.
02) 정렬한다.

# 첫번째 코드
import sys
input = sys.stdin.readline

def getIndex(s, val):
    global change

    ret = 0

    e = len(raw[1]) - 1
    while s <= e:
        mid = (s + e) // 2

        if raw[1][mid] < val:
            change = True
            ret = mid
            s = mid + 1
        else:
            e = mid - 1

    return ret

N, D = map(int, input().split())
raw = [[] for _ in range(3)]
for _ in range(N):
    idx, val = map(int, input().split())
    raw[idx].append(val)
for i in range(3):
    raw[i].sort()

ans = 0     # 돌파한 방의 개수
cur = 0     # 현재 위치한 몬스터의 방
ability = D
cnt = 0     # 장비 사용 개수
prv = -1
while True:
    if cur == len(raw[1]) and cnt == len(raw[2]):
        break

    change = False
    cur = getIndex(cur, ability) + 1   # cur까지 이동한다.

    if prv >= cur and cnt != len(raw[2]):          # 현재 능력치로 더 이상 몬스터를 처치할 수 없다면,
        ability *= raw[2][cnt]
        cnt += 1
        ans += 1
        continue
    elif not change and cnt != len(raw[2]):
        ability *= raw[2][cnt]
        cnt += 1
        ans += 1
        continue
    elif prv >= cur and cnt == len(raw[2]):         # 현재 능력치로 더 이상 몬스터를 처치할 수 도 없고 사용할 장비도 없다면,
        break
    if raw[1][cur - 1] >= ability:
        break

    ans += cur - (prv + 1)
    ability += sum(raw[1][prv + 1:cur])

    prv = cur - 1

print(ans)
"""