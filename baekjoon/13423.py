"""
완전탐색으로 먼저생각해보자
1. 주어진 점들로 만들 수 있는 모든 경우를 다 탐색한다.
    - N이 1,000개가 주어지면 경우의 수가 1,000 * 999 * 998

최적화하기, 하나의 점으로 후보군을 판별한다.
1. 점들을 정렬한다.
2. 점들을 순회한다. 특정 점을 기준으로 다음 점과, 이전 점의 간격이 동일하면 카운팅한다.
"""
import sys
input = sys.stdin.readline

Q = int(input())
while Q:
    Q -= 1
    N = int(input())
    raw = sorted(list(map(int, input().split())))
    ans = 0

    for i in range(N):
        if i - 1 < 0 or i + 1 > N:
            continue

        s = i - 1
        e = i + 1

        while 0 <= s and e <= N-1:
            if abs(raw[s]-raw[i]) == abs(raw[e]-raw[i]):
                ans += 1
                s -= 1
                e += 1
            elif abs(raw[s]-raw[i]) < abs(raw[e]-raw[i]):
                s -= 1
            else:
                e += 1
    
    print(ans)