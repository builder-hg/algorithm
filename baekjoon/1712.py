import sys
input = sys.stdin.readline

# ans = 0
# s = 1
# e = 11

# while s <= e:
#     mid = (s + e) // 2
#     K = mid - 10

#     if K > 0:
#         ans = mid
#         e = mid - 1
#     else:
#         s = mid + 1

# print(ans)

A, B, C = map(int, input().split())
ans = 0
s = 1
e = 2100000000 + 10

if C <= B:
    print(-1)
    sys.exit()

while s <= e:
    mid = (s + e) // 2
    val = -A + ((C - B) * mid)

    if val > 0:
        ans = mid
        e = mid - 1
    else:
        s = mid + 1

print(ans)