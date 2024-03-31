import sys
input = sys.stdin.readline

N = int(input())
lst = [int(input()) for _ in range(N)]
ans = 0

if N == 1:
    print(0)
    sys.exit()

while lst[0] <= max(lst[1:]):
    max_index = lst[1:].index(max(lst[1:])) + 1
    lst[0] += 1
    lst[max_index] -= 1
    ans += 1

print(ans)