"""
1. 풀이전략, 템플릿3
1) 정렬된 문자열을 순회하며 조건을 만족하는 문자열을 출력한다.

2. 구현, 설계
2-1. 로직
1) 문자열을 정렬한다.
2) 문자열을 순회한다. 이 때 다음 문자열의 순회위치는 이전 문자열 순회위치 + 1이다
3) 문자열을 L개까지 만들었다면 조건에 부합하는 지 확인한다.
4) 답이 될 수 있는 문자열을 출력한다.

2-2. 코드
1) 재귀함수 인자
- 현재함수내에서의 순회위치 i, 다음 재귀에서 i+1부터 시작하기 위함이다.
- cur, 1씩 증가하며 전달한다.
2) 조건
- 모음(a, e, i, o, u)이 하나 이상 존재해야 한다.
- 자음이 2개 이상 존재해야 한다.
"""
import sys
input = sys.stdin.readline

K, N = map(int, input().split())
arr = sorted(input().split())
ans = ['' for _ in range(K)]
vowels = ['a', 'e', 'i', 'o', 'u']

def check(cur):
    if cur != K:
        return True
    
    vowels_cnt = 0
    consonants_cnt = 0

    for i in range(K):
        if ans[i] in vowels:
            vowels_cnt += 1
            continue
        consonants_cnt += 1

    if vowels_cnt == 0 or consonants_cnt < 2:
        return False
    
    return True

def recur(cur, start):
    # 가지치기
    if not check(cur):
        return

    # 기저조건
    if cur == K:
        print(*ans, sep="")
        return

    # 재귀호출
    for i in range(start, N):
        ans[cur] = arr[i]
        recur(cur + 1, i + 1)

recur(0,0)