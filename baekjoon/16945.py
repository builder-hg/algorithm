"""
0. 문제이해
- 배열의 크기 3 * 3 
- 매직스퀘어로 변경하는 비용의 최솟값 도출
- 사용되는 숫자 1 ~ 9

1. 문제풀이설계, 로직
1) 각각의 자리를 순회한다.
2) 현재 위치한 지점의 값을 1부터 9까지 넣어본다.
3) 설정한 값을 기반으로 다음 경우를 살펴본다. 
4) 조건을 만족하는 지점의 값과 기존 값의 차이를 구한다.
5) 차이의 합과 기존 ans를 비교하여 더 작은 쪽으로 갱신한다.

1-2. 문제풀이설계, 변수
1) 변수
- arr
    : 크기가 3*3인 2차원 배열
- copy_arr
    : 크기가 3*3인 2차원 배열, 
    : 지정한 특정 값을 담을 배열
- visited
    : 방문처리를 관리할 배열
    : 1~10 중 하나를 사용하면 다음에 사용하지 못하도록 한다.
- ans
    : 비용의 최솟값

2) 재귀함수 인자
- x : 2차원 배열의 행에 해당한다.
- y : 2차원 배열의 열에 해당한다.
- expense : 비용에 해당한다.

3) 조건
3-0) 가지치기조건
- 행의 모든 원소 합은 15여야한다.
- 열의 모든 원소 합은 15여야 한다.
- 대각선의 모든 합은 15여야 한다.
3-1) 기저조건
- x가 3이 될 때 전체를 다 둘러보았다는 의미다.
- 이 때 최솟값을 갱신한다.

4) 재귀호출
- 방문처리 
- 카피본에 1 ~ 9 중 하나의 값을 지정하여 살펴본다.
"""
import sys
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(3)]
copy_arr = [[0 for _ in range(3)] for _ in range(3)]
visited = [False for _ in range(10)]
ans = 1 << 64

def check():
    # 행의 합
    for i in range(3):
        total = 0
        for j in range(3):
            total += copy_arr[i][j]
        if total != 15:
            return False

    # 열의 합
    for j in range(3):
        total = 0
        for i in range(3):
            total += copy_arr[i][j]
        if total != 15:
            return False

    # 대각선의 합1
    if copy_arr[0][0] + copy_arr[1][1] + copy_arr[2][2] != 15: return False

    # 대각선의 합2
    if copy_arr[0][2] + copy_arr[1][1] + copy_arr[2][0] != 15: return False

        
    return True

def recur(x, y, expense):
    global ans
    # 이동
    if y == 3:
        x += 1
        y = 0

    # 기저조건
    if x == 3:
        # 가지치기
        if not check():
            return
        
        ans = min(ans, expense)
        return
    
    # 재귀호출
    for i in range(1, 10):
        if visited[i]:
            continue

        visited[i] = True
        copy_arr[x][y] = i
        recur(x, y+1, expense + abs(arr[x][y] - i))
        visited[i] = False


recur(0, 0, 0)
print(ans)