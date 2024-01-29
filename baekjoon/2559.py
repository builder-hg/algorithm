"""
문제풀이전략

- 정답 : 가장 큰 구간합 출력 => 구간 get query
- 과정
1) 누적합 배열을 만든다.
2) s, e를 이동하면서 가장 큰 구간의 값을 구한다. prefix[e] - prefix[s], 구간의 길이는 K이다.
"""
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
raw = [0] + list(map(int, input().split()))
prefix = [0 for _ in range(N+1)]
for i in range(1, N+1):
    prefix[i] = prefix[i-1] + raw[i]

ans = -(1 << 64)
for i in range(K, N+1):
    temp = prefix[i] - prefix[i-K]
    ans = max(ans, temp)
print(ans)