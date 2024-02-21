"""
0. 문제이해
- N개의 수, 수열 a1, a2, ..., an
- N-1개의 연산자, +, -, *, /

1. 풀이전략, 로직
- 템플릿 1 or 2
1) N-1개의 연산자의 순서쌍을 구한다.
    - 위치에 영향을 받으며
    - 중복되어서는 안된다.
2) 순서쌍과 주어진 숫자를 차례로 대입하며 값을 구한다.
3) 구한 값을 최댓값과 최솟값과 비교하며 갱신한다.

2. 풀이전략, 코드
1) 변수
- arr[]
    : 크기 N
    : 수가 담길 배열
- ans[]
- ans[]
    : 크기 N-1
    : 연산자가 담길 배열
- visited[]
    : 크기 N-1
    : 방문처리
- max_value
    :초기값 1<<64
- min_value
    : 초기값 1>> 64
2) 재귀함수 인자
- cur
    : 현재까지 몇개의 연산자를 답에 담았는 지에 관한 개수
3) 기저조건
- cur가 N이 되었을 때,
- N-1까지 순회하며 arr[i], ans[i], ..., arr[N-2], ans[N-2], arr[N-1]의 값을 계산한ㄷ.ㅏ
- 최댓값, 최솟값과 비교하며 갱신한다. 
"""
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
cnt_lst = list(map(int, input().split())) # +, -, *, //
operator =[]
for i in range(4):
    for _ in range (cnt_lst[i]):
        if i == 0:
            operator.append('+')
        elif i == 1:
            operator.append('-')
        elif i == 2:
            operator.append('*')
        else:
            operator.append('//')
ans = ['' for _ in range(N-1)]
visited = [False for _ in range(N-1)]
min_value = (1 << 64)
max_value = -(1 << 64)


def recur(cur):
    global min_value
    global max_value

    # 기저조건
    if cur == N-1:
        val = arr[0]
        for i in range(1, N):
            if ans[i-1] == '+':
                val += arr[i]
            elif ans[i-1] == '-':
                val -= arr[i]
            elif ans[i-1] == '*':
                val *= arr[i]
            elif ans[i-1] == '//':
                if val < 0:
                    val = -(abs(val) // arr[i])
                else:
                    val //= arr[i]
        
        if val > max_value:
            max_value = val
        if val < min_value:
            min_value = val

        return
    
    # 재귀호출
    for i in range(len(operator)):
        if visited[i]:
            continue

        visited[i] = True
        ans[cur] = operator[i]
        recur(cur + 1)
        visited[i] = False


recur(0)
print(max_value)
print(min_value)