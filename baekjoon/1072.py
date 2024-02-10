
import sys
input = sys.stdin.readline

X, Y = map(int, input().split())
Z = (100 * Y) // X 
ans = 0
s = 0
e = X

if Z >= 99:
    print(-1)
    sys.exit()

while s <= e:
    mid = (s + e) // 2

    if (100 * (Y + mid)) // (X + mid) > (100 * Y) // X :
        ans = mid
        e = mid - 1
    else:
        s = mid + 1

print(ans)