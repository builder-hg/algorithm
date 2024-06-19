"""
10, 3
3 3 4

1 <= K <= 20
1 <= S <= 100

10 // 3 => 3 .. 1
10 // 4 => 2 .. 2
13 // 8 => 1 .. 5
10 // 10 => 1 .. 0

"""
import sys
input = sys.stdin.readline

S, K = map(int, input().split())

share = S // K   # 몫
r = S % K   # 나머지
lst = []
for i in range(K):
    lst.append(share)
for i in range(len(lst)):
    if r == 0:
        break

    lst[i] += 1
    r -= 1

ans = 1
for i in range(len(lst)):
    ans *= lst[i]

print(ans)
