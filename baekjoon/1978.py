import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
rest = N
ans = 0

def getPrime(num):
    cnt = 0

    if num == 1:
        return 0

    for i in range(1, num + 1):
        if i * i > num:
            break
        if num % i == 0:
            cnt += 1
            
    if cnt == 1:
        return 1
    else:
        return 0

for i in range(N):
    ans += getPrime(arr[i])

print(ans)