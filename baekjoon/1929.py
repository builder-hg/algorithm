import sys
input = sys.stdin.readline

M, N = map(int, input().split())
isPrime = [True for i in range(N+1)]

isPrime[0] = False
isPrime[1] = False

for i in range(2, N+1):
    if not isPrime[i]:
        continue
    for j in range(i*i, N+1, i):
        isPrime[j] = False

for i in range(M):
    isPrime[i] = False

for i in range(N+1):
    if isPrime[i]:
        print(i)
"""
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
ans = []

def check(num):
    cnt = 0
    for i in range(1, num + 1):
        if i * i > num:
            break
        if num % i == 0:
            cnt += 1
    
    if cnt == 1:
        return num
    else:
        return -1

for i in range(M, N+1):
    res = check(i)
    if res != -1: ans.append(res)

for i in range(len(ans)):
    print(ans[i])
"""