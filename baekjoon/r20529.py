import sys
input = sys.stdin.readline

Q = int(input())
while Q:
    Q -= 1
    N = int(input())
    arr = list(input().split())
    ans = 1 << 64
    
    if N > 32:
        print(0)
        continue

    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                a = arr[i]
                b = arr[j]
                c = arr[k]

                cnt = 0
                for idx in range(4):
                    if a[idx] == b[idx] == c[idx]: continue
                    cnt += 2
                ans = min(ans, cnt)

    print(ans)