import sys
input = sys.stdin.readline

N, K = map(int, sys.stdin.readline().split())
arr = sorted(list(map(int, input().split())))
ans = 0
ans += arr.count(K)
arr = arr[:N-ans]
s = 0
e = len(arr)-1
rest = len(arr)

while s < e:
    if arr[s] + arr[e] >= K / 2:
        ans += 1
        rest -= 2
        s += 1
        e -= 1
    else:
        s += 1
    
ans = ans + (rest // 3)
print(ans)