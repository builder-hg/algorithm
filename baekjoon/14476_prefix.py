import sys
input = sys.stdin.readline

N = int(input())
raw = list(map(int, input().split()))
ans = []

prefix_gcd = [0 for _ in range(N+1)]
suffix_gcd = [0 for _ in range(N+1)]

prefix_gcd[0] = raw[0]
suffix_gcd[N-1] = raw[N-1] 
for i in range(1, N):
    numA = prefix_gcd[i-1]
    numB = raw[i]
    while numB:
        numA, numB = numB, numA % numB
    prefix_gcd[i] = numA
for i in range(N-2, -1, -1):
    numA = suffix_gcd[i+1]
    numB = raw[i]
    while numB:
        numA, numB = numB, numA % numB
    suffix_gcd[i] = numA

for i in range(N):
    numA = prefix_gcd[i-1]
    numB = suffix_gcd[i+1]
    while numB:
        numA, numB = numB, numA % numB
    if raw[i] % numA == 0:
        continue
    ans.append((numA, raw[i]))
ans.sort()
if (ans):
    print(*ans[0])
else:
    print(-1)