import sys
input = sys.stdin.readline

visited = [False for _ in range(10001)]
visited[0] = True

def generate(N):
    temp = N
    total = N
    while temp:
        total += temp % 10
        temp //= 10

    if total >= 10001: return

    visited[total] = True
    generate(total)
    
    return 

for i in range(1, 10001):
    if visited[i]:
        continue

    print(i)
    generate(i)