"""import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

i = 0 
for j in range(1, N):
    if arr[i] != arr[j]:
        print((str(j+1)+' ')*(j-i), end='')
        i = j
print(('-1 ')*(N-i), end='')"""

"""
import sys
input = sys.stdin.readline

N = int(input())
arr = [0] + list(map(int, input().split()))
ans = [-1 for _ in range(N)]
res = -1
for i in range(N-1, 0, -1):
    if arr[i] != arr[i+1]:
        res = i + 2
    ans[i] = res

print(*ans)
"""
"""
import sys
input = sys.stdin.readline

N = int(input())
arr = [0] + list(map(int, input().split()))
ans = [-1 for _ in range(N)]
res = -1
for i in range(1, N)[::-1]:
    if arr[i] != arr[i+1]:
        res = i + 2
    ans[i] = res

print(*ans)
"""

# print(*ans[::-1])

