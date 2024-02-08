"""
4 8 12 16 20
12를 뺀다고했을때
4와 8처럼 12의 약수이면 안됨 

4 8 11 16 20
11를 뺀다고 했을 때 
남은 수들이 11의 약수가 아니다.

"""
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
gcd = 1 << 64
val = -1

front = [0] * (N+1)
front[0] = arr[0]
rear = [0] * (N+1)
rear[N-1] = arr[N-1]

for i in range(1, N):
    prev = front[i-1]
    cur = arr[i]
    while cur:
        prev, cur = cur, prev % cur
    front[i] = prev

for i in range(N-2, -1, -1):
    next = rear[i+1]
    cur = arr[i]
    while cur:
        next, cur = cur, next % cur
    rear[i] = next

front = [0] + front 
rear = rear + [0]
for i in range(N):
    numA = front[i-1]
    numB = rear[i+1]
    while numB:
        numA, numB = numB, numA % numB
    
    if arr[i] % numA == 0:
        continue
    
    if numA <= gcd:
        gcd = numA
        val = arr[i]

if val == -1:
    print(-1)
else:
    print(gcd, val)
