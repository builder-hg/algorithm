"""
1. 완전탐색, 주어진 점들로 만들 수 있는 모든 경우를 다 탐색한다.
    - 세가지 점을 고르는 경우.
    - N이 1,000개가 주어지면 경우의 수가 1,000 * 999 * 998

2. 최적화하기, 이진탐색으로 점을 어떻게 줄여가면서 볼 수 있을까.
2-1. 관찰케이스
[-4 -1 0 2 4]
- 점 두개를 고른다. (1000*1000), 
- 각 지점의 값의 차를 구한다.
    -4, 0이면 차는 -4이고 three dot을 성립하려면 -2를 가지고 있어야한다.
    - 수열에 -2가 있는지 확인하고 있으면 ans를 1증가시킨다
        => n * n * len(arr), 시간초과


3. 방법
3-1. 점들을 정렬한다.
3-2. 두 점을 고르고 한 점을 이진탐색으로 선택한다.

0. 고민
- 후보의 범위를 줄이는 과정에서 이진탐색을 쓴다고 했을 때,
    q) 어떤 부분에서 이진탐색을 쓸 수 있을까

"""
import sys
input = sys.stdin.readline

Q = int(input())

def check(s, e, val):
    while s <= e:
        mid = (s + e) // 2

        if raw[mid] == val:
            return True
        elif raw[mid] < val:
            s = mid + 1
        else:
            e = mid - 1

    return False

while Q:
    Q -= 1

    N = int(input())
    raw = sorted(list(map(int, input().split())))
    ans = 0
    
    s = 0
    e = N - 1

    for i in range(N):
        for j in range(i+1, N):
            val = (raw[i] + raw[j]) // 2
            if val - raw[i] != raw[j] - val:
                continue
            if check(i, j, val):
                ans += 1

    print(ans)