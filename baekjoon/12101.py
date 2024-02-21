"""
1. 문제풀이, 템플릿1
- [1, 2, 3]을 순회하며 cur이 1부터 N까지 살펴본다.
- 조건을 만족하는 지 살펴본다.
- 답이될 수 있는 경우를 저장한다.
- 경우들을 정렬한 후 K-1번째에 위치한 식을 출력한다.

2. 코드
0) 변수
- ans 배열의 크기는 N이다. 기본값은 0이다.
    ans[cur] = i # 1, 2, 3 
- candid
1) 가지치기
- total이 N보다 크다면 False를 반환한다.
2) 인자
- cur, 답을 담은 개수
- total, 현재까지 담은 값들의 총합
3) 기저조건
- ans에들어있는 인자들을 +로 결합하여 candid 변수에 담는다.
4) 출력
- candid를 정렬하여 K-1번째를 출력한다.

"""
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
ans = [0 for _ in range(N)]
candid = []

def check(cur, total):
    if cur < 1:
        return True
    
    if total > N:
        return False
    
    return True

def recur(cur, total):
    if not check(cur, total):
        return
    
    if total == N:
        candid.append('+'.join(ans[:cur]))
        return
    
    for i in range(1, 4):
        ans[cur] = str(i)
        recur(cur + 1, total + i)

recur(0, 0)
candid.sort()
if len(candid) < K:
    print(-1)
else:
    print(candid[K-1])