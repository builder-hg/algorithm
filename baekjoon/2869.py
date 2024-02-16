"""
0. 특징관찰
- 하루에 + A, - B 
- N일, (A - B) * (N - 1) + A == V
"""
import sys
input = sys.stdin.readline

A, B, V = map(int, input().split())
s = 1
e = 1000000001
ans = 0
while s <= e:
    mid = (s + e) // 2
    if (A - B) * mid >= V - B:
        ans = mid
        e = mid - 1
    else:
        s = mid + 1

print(ans)